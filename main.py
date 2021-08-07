import ocrmypdf
from os import listdir, getcwd

SOURCE_PATH = f"{getcwd()}/source_files"
DESTINATION_PATH = f"{getcwd()}/destination_files"

for item in listdir(SOURCE_PATH):
    output_name = item.lower().replace(" ","_").replace(".","_").replace("_pdf", ".pdf")
    input_file = f"{SOURCE_PATH}/{item}"
    output_file = f"{DESTINATION_PATH}/{output_name}"

    ocrmypdf.ocr(input_file, output_file, language="spa+eng", optimize=3, clean=True, progress_bar=False, rotate_pages=True, deskew=True, jobs=4)



