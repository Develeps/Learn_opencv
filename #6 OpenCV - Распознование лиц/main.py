import cv2 
import numpy as np 

img = cv2.imread('images/5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('face.xml')

result = faces.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)

for (x, y, w, h) in result:
    cv2.rectangle(img, (x, y), (x+w,y+h), (0, 255, 0), thickness=3)

cv2.imshow("result", img)
cv2.waitKey(0)