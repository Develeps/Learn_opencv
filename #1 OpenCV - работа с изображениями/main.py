from multiprocessing.connection import wait
import cv2 
import numpy as np

img = cv2.imread("image/stop.jpg")

#-------------------------------------------------------------
re_img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
#cv2.imshow("result",re_img[0:400, 0:450])

#-------------------------------------------------------------
#blur_img = cv2.GaussianBlur(re_img, (201,201), 0)
#cv2.imshow("blur", blur_img)

#-------------------------------------------------------------
#img_col = cv2.cvtColor(re_img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("silver", img_col)

#-------------------------------------------------------------

"""
arr = np.ones((2, 2), np.uint8)
img_v = cv2.Canny(re_img, 200, 200)
img_v = cv2.dilate(img_v, arr, iterations=1)
img_v = cv2.erode(img_v, arr, iterations=1)

cv2.imshow("bW", img_v[0:500][0:500])
"""
#cv2.waitKey(0)

#-------------------------------------------------------------
"""
video = cv2.VideoCapture("video/1.mp4")

while True:
    mess, fram = video.read()
    cv2.imshow("vid", fram)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break 
"""

#-------------------------------------------------------------
"""
camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 540)

while True: 
    mess, fram = camera.read()
    cv2.imshow("Cmaera", fram)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
"""
#-------------------------------------------------------------


img_1 = cv2.imread('image/car.jpg')
img_2 = cv2.imread('image/stop.jpg')

x = 0
y = 800
res = cv2.addWeighted(img_1[0+x:800+x, 0+y:800+y], 1, img_2[0+x:800+x,0+y:800+y], 1, 0)

cv2.imshow("res", res)
cv2.waitKey(0)





#print(img.shape)

'''
car = cv2.imread("image/car.jpg")

result = cv2.addWeighted(img, 0.9, car, 0.1)

cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
