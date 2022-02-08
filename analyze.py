import pytesseract
from PIL import Image

verification_img = Image.open(r'.\tmp\verification_img.png')
verification_text = pytesseract.image_to_string(verification_img)
print(verification_text)