import re
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup as bs

# Load EPUB book
filepath = "/Users/ricky/digital_texts/corpus/processing/image_plaintext/epub/chamoru_legends.epub"
book = epub.read_epub(filepath)

# Extract metadata for TEI header
title = book.get_metadata("DC", "title")
author = book.get_metadata("DC", "creator")
date_of_publication = book.get_metadata("DC", "date")

title = book.get_metadata("DC", "title")[0][0] if title else "CHamoru Legends "
author = (
    book.get_metadata("DC", "creator")[0][0] if author else "Teresita Lourdes Perez"
)
date_of_publication = (
    book.get_metadata("DC", "date")[0][0] if date_of_publication else "Unknown Date"
)

tei_header = f"""
<teiHeader>
    <fileDesc>
        <titleStmt>
            <title>{title}</title>
            <author>{author}</author>
        </titleStmt>
        <publicationStmt>
            <date>{date_of_publication}</date>
        </publicationStmt>
    </fileDesc>
</teiHeader>
"""

# First pass to extract text
with open("chamoru_legends.txt", "w", encoding="utf8") as output:
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            html_doc = item.get_content()
            soup = bs(html_doc, "html.parser")
            for tag in soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"]):
                output.write(f"<{tag.name}>{tag.get_text(strip=True)}</{tag.name}>\n")

# Second pass to structure TEI body
tei_body = ""
in_text = False
in_div1 = False
in_div2 = False
part_heading = ""

with open("chamoru_legends.txt", "r", encoding="utf8") as input_file:
    for line in input_file:
        if "<p>Part First" in line:
            in_text = True

        if in_text:
            if part_heading:
                if in_div1:
                    tei_body += "</div2></div1>\n"
                part_heading = part_heading.strip("<p>").strip("</p>").strip()
                tei_body += f"<div1><head>{part_heading}</head>\n"
                in_div1 = True
                in_div2 = False
                part_heading = ""
                continue

            chapter_match = re.search(r"Chapter ([A-Z]+)", line)
            if chapter_match:
                chapter_number = chapter_match.group(1)
                if in_div2:
                    tei_body += "</div2>\n"
                tei_body += f"<div2><head>Chapter {chapter_number}</head>\n"
                in_div2 = True
                continue

            part_match = re.search(r"<p>(Part .*)</p>", line)
            if part_match:
                part_heading = part_match.group(1)
                continue

            if "<p>KINONSUTTAN I CHE'CHO'</p>" in line:
                break

            tei_body += line

# Final TEI XML output
tei_output = f"""<?xml version="1.0" encoding="UTF-8"?>
<TEI xmlns="http://www.tei-c.org/ns/1.0">
{tei_header}
<text>
    <body>
        {tei_body}
    </body>
</text>
</TEI>
"""

# Write the TEI output to a file
with open("chamoru_legends.tei.xml", "w", encoding="utf8") as tei_file:
    tei_file.write(tei_output)

print("TEI XML file has been generated: chamoru_legends.tei.xml")
