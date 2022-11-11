import cv2
import imutils
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#nr de inmatriculare = MH14WOW
img = cv2.imread(r'C:\Users\marcu\Desktop\Facultate\AI\inmatriculare.jpg')
img= cv2.resize(img,(800,600))
cv2.imshow('Imagine redimensionata',img)
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('imaginea grayscale',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()