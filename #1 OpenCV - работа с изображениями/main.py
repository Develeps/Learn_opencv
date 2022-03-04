import cv2 
import numpy as np

img = cv2.imread("image/stop.jpg")

re_img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
#cv2.imshow("result",re_img[0:400, 0:450])

#blur_img = cv2.GaussianBlur(re_img, (201,201), 0)
#cv2.imshow("blur", blur_img)

#img_col = cv2.cvtColor(re_img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("silver", img_col)


arr = np.ones((2, 2), np.uint8)
img_v = cv2.Canny(re_img, 200, 200)
img_v = cv2.dilate(img_v, arr, iterations=1)
img_v = cv2.erode(img_v, arr, iterations=1)

cv2.imshow("bW", img_v)





cv2.waitKey(0)


#print(img.shape)

'''
car = cv2.imread("image/car.jpg")

result = cv2.addWeighted(img, 0.9, car, 0.1)

cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
