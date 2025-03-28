import pytesseract
from bs4 import BeautifulSoup as bs

# setting the path to the Tessearct binary
pytesseract.pytesseract.tesseract_cmd = r"/opt/homebrew/bin/tesseract"

# generate the range of pages we want to work with
page_images = range(1, 388)

with open(
    "the_island_of_the_colour_blind_and_cycad_island.txt", "w", encoding="utf8"
) as output:
    for page in page_images:
        page_path = f"/Users/ricky/digital_texts/corpus/processing/images_files/The_island_of_the_colour_blind_and_Cycad_Island_images/page-{page}.tiff"
        print(f"Processing {page_path} ...")  # to keep track of progress
        xml = pytesseract.image_to_alto_xml(page_path)
        soup = bs(xml, "xml")
        text_blocks = soup.find_all("TextBlock")  # text block is typically a paragraph
        for text_block in text_blocks:
            text_lines = text_block.find_all(
                "TextLine"
            )  # text line is typically line within each block
            paragraph = []
            for text_line in text_lines:
                string_tags = text_line.find_all("String")  # find each word
                line = []
                for string_tag in string_tags:
                    line.append(string_tag["CONTENT"])
                line_of_text = " ".join(line)
                paragraph.append(line_of_text)
            paragraph_text = "\n".join(paragraph)
            output.write(f"{paragraph_text}\n\n")
        output.write("\n\n")
