import numpy as np
import cv2
import math

Video_capture = cv2.VideoCapture(1)
horizCenter = 320
vertiCenter = 240
targetWidth = 2
targetHeight = 500
focalLength = 700
imageTarWidth = None
imageTarHeight = None
rectCenterX = None
rectCenterY = None
maxX = 0.0
minX = 20000.0
maxY = 0.0
minY = 20000.0

while(True):

        cv2.namedWindow('Live', cv2.WINDOW_AUTOSIZE)

        ret,frame = Video_capture.read()
        horizCenter = np.size(frame, 0)/2
        print (horizCenter)
        verticenter = np.size(frame, 1)/2
        print ("Made it 1")
        hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        print ("Made it 2")
        THRESHOLD_MIN = np.array([53, 5, 228],np.uint8)
        THRESHOLD_MAX = np.array([58, 255, 238],np.uint8)

        print ("Made it 3")
        frame_threshed = cv2.inRange(hsv_img, THRESHOLD_MIN, THRESHOLD_MAX)

        #h, s, v = cv2.split(hsv_img)
        #s.fill(255)
        #v.fill(255)

        #Hsv_image = cv2.merge([h,s,v])
        print (frame)
        print (frame_threshed)
        #ret, lowerImg = cv2.threshold(h, 30, 255, cv2.THRESH_BINARY)
        #ret, upperImg = cv2.threshold(h, 30, 255, cv2.THRESH_BINARY_INV)

        #h = lowerImg & upperImg

        #frame_threshed = cv2.merge((h, s, v))
        print ("Made it 4")
        cv2.imshow('Live', frame_threshed)
        #cv2.imshow('Live', frame)
        print ("Made it 5")
        key = cv2.waitKey(10)
        if key == 27:
          cv2.destroyWindow("Live Feed")
          cv2.destroyWindow('Contours')
          cv2.destroyWindow('Threshed')
          break
