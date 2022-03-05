import cv2 
import numpy as np 

#----------------------------------------------------
"""
a = np.zeros((480, 640, 3), dtype='uint8')
a[100:200, 100:200] = 120, 0, 0

cv2.imshow("array", a)
cv2.waitKey(0)
"""

#----------------------------------------------------
a = np.zeros((480, 640, 3), dtype='uint8')

cv2.rectangle(a, (0,0), (100, 100), (255, 0, 0), thickness=2)

#cv2.line(a, (100, 100),(200, 200),(255, 200, 0), thickness=2)

cv2.line(a, (0, a.shape[0]//2),(a.shape[1]//2, a.shape[0]//2),(255, 200, 0), thickness=2)

cv2.circle(a, (a.shape[1]//2,a.shape[0]//2), 50 ,(0, 0 ,100), thickness=cv2.FILLED)

cv2.putText(a, "hello SUGU", (100, 200), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 220), thickness=2)



cv2.imshow("cube" ,a)
cv2.waitKey(0)
