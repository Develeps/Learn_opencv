import cv2 
import numpy as np 



camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 540)

while True: 
    mess, img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = cv2.CascadeClassifier('face.xml')
    result = faces.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in result:
        cv2.rectangle(img, (x, y), (x+w,y+h), (0, 255, 0), thickness=3)

    cv2.imshow("Cmaera", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
