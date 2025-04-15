import pytesseract
from PIL import Image
from io import BytesIO



import  os

# def open_screenshot():
    
    # return screenshotpath
# def getcaptcha(self):
# im = Image.open(BytesIO(captch))
# im.save(r'C:/Users/deepa/Desktop/deepa/JustRecharge/images_or_text/cap.png')
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
screenshotpath = os.path.join(os.path.sep, ROOT_DIR,)
print (screenshotpath)
pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
image = Image.open(screenshotpath+r'/cap.png',mode='r')
result = pytesseract.image_to_string(image)
with open('abc.txt',mode='w') as file:
    file.write(result)
#driver.implicitly_wait(4)
files = open('abc.txt')
str = files.read().replace("=",'')
# str = str.replace("+",',').split(',')
# st = int(str[0]) + int(str[1])
st=int(eval(str))
print(st)

