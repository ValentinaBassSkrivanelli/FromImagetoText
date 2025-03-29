from PIL import Image
import pytesseract



pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR'


img = Image.open("image11.png")

result = pytesseract.image_to_string(img)

print(result)
