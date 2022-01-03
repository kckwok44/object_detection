from PIL import Image
from os import listdir

PATH = "/Users/benkwok/table_detection/borderless_tbls_detection/images/all_images"

for file in listdir(PATH):
    if file.endswith("png"):
        image = Image.open(f"{PATH}/{file}")
        new_image = file.replace(".png", ".jpg")
        image.save(f"{PATH}/{new_image}")
