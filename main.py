# PIL is pillow and is a basic image processing library
from PIL import Image 

import pytesseract

print(pytesseract.image_to_string(Image.open("screenshot.png")))

