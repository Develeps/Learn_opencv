from pydoc import apropos
import cv2
from cv2 import sort 
import numpy as np 
import imutils
import easyocr 
from matplotlib import pyplot as plt


img = cv2.imread("images/2.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_filter = cv2.bilateralFilter(gray, 11, 15, 15)
edges = cv2.Canny(img_filter, 30, 200)

cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cont = imutils.grab_contours(cont)
cont = sorted(cont, key=cv2.contourArea, reverse=True)


pos = None 
for c in cont: 
    approx = cv2.approxPolyDP(c, 15, True)
    if len(approx) == 4:
        pos = approx
        break

#print(pos)

mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
bit_img = cv2.bitwise_and(img, img, mask=mask)


(x, y) = np.where(mask==255)
(x1, y1) = np.min(x), np.min(y)
(x2, y2) = np.max(x), np.max(y)
crop = gray[x1:x2, y1:y2]


#ВАЖНО для этой программы требутеся CUDA а она подерживается только видеокартами NVIDIA
#Нашол как испарвить это на AMD
#для этого надо: pip install opencv-python==4.5.4.60

text = easyocr.Reader(["en"])
text = text.readtext(crop)

print(text[0])


plt.imshow(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
plt.show()