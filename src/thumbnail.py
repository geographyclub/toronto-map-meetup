import glob
from PIL import Image

input_folder = "data/from_client/PNGs"

for input_path in glob.glob(f"{input_folder}/*png"):
    pil_image: Image = Image.open(input_path)
    pil_image = pil_image.convert("RGBA")
    pil_image = pil_image.crop(pil_image.getbbox())

    # Reduce the image size
    size = 400, 250
    pil_image.thumbnail(size)
  
    pil_image.save(input_path)
