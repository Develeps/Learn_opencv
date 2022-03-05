import cv2 
import numpy as np 

"""
img = cv2.imread("images/2.jpg")
img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
"""

photo = cv2.imread("images/2.jpg")
photo = cv2.resize(photo, (photo.shape[1]//2,photo.shape[0]//2))

img = np.zeros((photo.shape[0],photo.shape[1]), dtype="uint8")

circle = cv2.circle(img.copy(), (550, 400), 180, 255, -1)
square = cv2.rectangle(img.copy(), (25, 25), (250, 250), 255, -1)


#img = cv2.bitwise_and(circle, square)
#img = cv2.bitwise_not(circle, square)
#img = cv2.bitwise_or(circle, square)
#img = cv2.bitwise_not(square)

img = cv2.bitwise_and(photo, photo, mask=circle)



cv2.imshow("result", img)
cv2.waitKey(0)