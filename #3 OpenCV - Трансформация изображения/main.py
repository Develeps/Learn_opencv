from hashlib import new
import cv2 
import numpy as np 


#----------------------------------------------
"""
img = cv2.imread("images/1.jpg")
img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
img = cv2.flip(img, 0)

cv2.imshow("res", img)
cv2.waitKey(0)
"""

#----------------------------------------------
"""
image =cv2.imread("images/2.jpg")

def rotate(img, angle):
    h, w = img.shape[:2]
    point = (w//2, h//2)
    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img, mat, (w, h))
image = cv2.resize(image, (image.shape[1]//2, image.shape[0]//2))
image = rotate(image, 90)

cv2.imshow("rotate", image)
cv2.waitKey(0)
"""

#----------------------------------------------
"""
img = cv2.imread("images/3.jpg")

def Transfomt(imp_p, x, y):
    mat = np.float32([[1, 0, x],[0, 1, y]])
    h, w = imp_p.shape[:2]
    return cv2.warpAffine(imp_p, mat,(w//2, h//2))

h, w = img.shape[:2]
#img = cv2.resize(img, (w//2, h//2))
img = Transfomt(img, 100, 100)

cv2.imshow("cat", img)
cv2.waitKey(0)
"""

#----------------------------------------------


img = cv2.imread("images/4.jpg")

new_img = np.zeros(img.shape, dtype="uint8")

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (5, 5), 0)

img = cv2.Canny(img, 100, 140)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

#print(com)

cv2.drawContours(new_img, con, -1, (255, 0, 0), 1)


#sum_img = cv2.addWeighted(img[0:500, 0:500], 1,  new_img[0:500, 0:500], 0.5 , 0)

cv2.imshow("cat", new_img)
cv2.waitKey(0)
