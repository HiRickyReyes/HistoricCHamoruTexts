import os
from pdf2image import convert_from_path

images = convert_from_path(
    "/Users/ricky/digital_texts/corpus/processing/pdfs/Legacy_of_a_Political_Union.pdf",
    fmt="tiff",
    dpi=400,
)

output_dir = "Legacy_of_a_Political_Union_images"
os.makedirs(output_dir, exist_ok=True)

page_count = 1
for image in images:
    page_image_name = os.path.join(output_dir, f"page-{page_count}.tiff")
    image.save(page_image_name, format="tiff")
    page_count += 1
