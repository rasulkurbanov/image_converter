import os
import sys
from PIL import Image
import glob

first = sys.argv[1]
second = sys.argv[2]

new_dir = "new"
parent_dir = "/media/rasul/766A9E0A6A9DC6F1/PET_PROJ/jpg_png_converter"
path = os.path.join(parent_dir, new_dir)


if not os.path.exists("new"):
    os.mkdir(path)


for filename in glob.glob("/media/rasul/766A9E0A6A9DC6F1/PET_PROJ/jpg_png_converter/Pokedex/*.jpg"):
    im = Image.open(filename)
    converted_img = im.convert('RGB')
    converted_img.save(f"{parent_dir}/{new_dir}/{filename[-14:-1]}.png", "PNG")





