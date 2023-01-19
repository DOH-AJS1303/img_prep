from PIL import Image, ImageOps
import os

img_loc = ""
sav_loc = img_loc + "Batch\\"
size = 600,800

def process(img_name, img_path, sav_loc, size):
    img = Image.open(img_path + img_name)
    img = img.rotate(90, expand=True)
    img = ImageOps.pad(image=img, size=size, method=Image.Resampling.LANCZOS)
    img.save(sav_loc + img_name)
   
images = os.listdir(img_loc)

for img_name in images:
    process(img_name, img_loc, sav_loc, size)
    
