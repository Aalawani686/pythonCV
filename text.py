import numpy as np
import cv2


cv2.namedWindow('Threshed', cv2.WINDOW_AUTOSIZE)

img = cv2.imread('text.png', -1)
THRESHOLD_MIN = np.array([90, 62, 144],np.uint8)
THRESHOLD_MAX = np.array([114, 255, 255],np.uint8)



hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
frame_threshed = cv2.inRange(hsv_img, THRESHOLD_MIN, THRESHOLD_MAX)
cv2.imshow("Threshed",frame_threshed)

src = cv2.cvtColor(frame_threshed, cv2.COLOR_GRAY2BGR)

tmp = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_,alpha = cv2.threshold(tmp,0,255,cv2.THRESH_BINARY_INV)
b, g, r = cv2.split(src)
rgba = [b,g,r, alpha]
dst = cv2.merge(rgba,4)
cv2.imwrite("test.png", dst)

while(cv2.waitKey(10) != 27):
    cv2.imshow('Threshed', dst)
