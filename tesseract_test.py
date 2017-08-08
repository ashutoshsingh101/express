from PIL import Image
import cv2
import pytesseract
import time


s = time.time()
img = cv2.imread("image/pdf_name01.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gay = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

cv2.imwrite("image/1.jpg",gray)

text = pytesseract.image_to_string(Image.open("image/1.jpg"))
print(text)
e = time.time()
print(str(e-s))
cv2.imshow("C",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
