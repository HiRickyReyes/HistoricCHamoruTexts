import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup as bs

filepath = "/Users/ricky/digital_texts/corpus/processing/epub/chamoru_legends.epub"
book = epub.read_epub(filepath)

title = book.get_metadata("DC", "title")
title_name = title[0][0] if title else "Unknown Title"
author = book.get_metadata("DC", "creator")
author_name = author[0][0] if author else "Unknown Author"
date = book.get_metadata("DC", "date")
date_of_publication = date[0][0] if date else "Unknown Date"

doc_content = book.get_items_of_type(ebooklib.ITEM_DOCUMENT)
full_text = ""

for content in doc_content:
    soup = bs(content.get_content(), "html")
    text = soup.get_text()
    full_text += text

with open("processed_chamoru_legends.txt", "w") as output_file:
    output_file.write(full_text)
