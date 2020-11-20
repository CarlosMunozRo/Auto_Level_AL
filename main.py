# Niveles automaticos Azur Lane

import re
import cv2
import pytesseract
from pytesseract import Output
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = 'confirm.png'
imge = Image.open(img)
data=pytesseract.image_to_string(imge)

print(data)pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'