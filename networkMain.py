import numpy as np
import cv2
import math
from socket import *
import sys
import network

soc = None
conn = None
connected = False

network1 = None
Video_capture = cv2.VideoCapture(0)
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

def angle(p1, p2, p0):
    dx1 = p1[0][0]-p0[0][0]
    dy1 = p1[0][1]-p0[0][1]
    dx2 = p2[0][0]-p0[0][0]
    dy2 = p2[0][1]-p0[0][1]
    #network1.setString(str(dx2).encode('utf-8'))
    return math.atan(dy1/dx1)-math.atan(dy2/dx2);

def processing(imageTarWidth, rectCenterX, rectCenterY):

        if imageTarWidth != None :
            #print(imageTarWidth)
            distance  = targetWidth * focalLength / imageTarWidth

            offsetX = abs(rectCenterX - horizCenter)
            offsetY = abs(rectCenterY - vertiCenter)

            azimuth = np.arctan(offsetX/ focalLength)*180/math.pi
            altitude = np.arctan(offsetY/ focalLength)*180/math.pi
            print ('Distance' + str(distance))
            print ('Azimuth' + str(azimuth))
            print ('Altitude' + str(altitude))


            network1.setDistance(str(distance).encode('utf-8'))
            network1.setAzimuth(str(azimuth).encode('utf-8'))
            network1.setAltitude(str(altitude).encode('utf-8'))

            imageTarWidth = None
            imageTarHeight = None
            rectCenterX = None
            rectCenterY = None

#def __init__(self):
global network1
network1 = network.Network()
network1.userServer()



while(True):

    cv2.namedWindow('Threshed', cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("Live Feed", cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow('Contours', cv2.WINDOW_AUTOSIZE)

    ret,frame = Video_capture.read()
    horizCenter = np.size(frame, 0)/2
    verticenter = np.size(frame, 1)/2

    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    THRESHOLD_MIN = np.array([53, 5, 228],np.uint8)
    THRESHOLD_MAX = np.array([58, 255, 238],np.uint8)

    frame_threshed = cv2.inRange(hsv_img, THRESHOLD_MIN, THRESHOLD_MAX)

    #h, s, v = cv2.split(hsv_img)
    #s.fill(255)
    #v.fill(255)

    #Hsv_image = cv2.merge([h,s,v])

    #ret, lowerImg = cv2.threshold(h, 30, 255, cv2.THRESH_BINARY)
    #ret, upperImg = cv2.threshold(h, 30, 255, cv2.THRESH_BINARY_INV)

    #h = lowerImg & upperImg

    #frame_threshed = cv2.merge((h, s, v))

    cv2.imshow('Threshed', frame_threshed)

    image, contours, hierarchy = cv2.findContours(frame_threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    count = -1
    for cont in contours:
        count = count + 1
        epsilon = 0.1*cv2.arcLength(cont, True)
        approx = cv2.approxPolyDP(cont, epsilon, True)

        if cv2.contourArea(approx) > 5000 and len(approx) == 4:
            #print (len(approx))
            #print (cv2.contourArea(approx))

            cv2.drawContours(image, contours, count, (255,255,255), 10)
            maxCosine = 0
            for k in range(2, 5):

                    pt1 = approx[k%4]
                    pt2 = approx[k-2]
                    pt0 = approx[k-1]
                    cos = (angle(pt1, pt2, pt0))
                    cosine = math.fabs(math.cos(cos))

                    maxCosine = max(maxCosine, cosine)
            #print (maxCosine)

            if(maxCosine<.2):

                #print ('entered')

                for i in approx:

                    #print (i[0][0])
                    #print (i[0][1])
                    if i[0][0]>maxX:
                        global maxX
                        maxX = i[0][0]
                        #print ('maxX')

                    if i[0][0]<minX:
                        global minX
                        minX = i[0][0]
                        #print ('minX')

                    if i[0][1]>maxY:
                        global maxY
                        maxY = i[0][1]
                        #print ('maxY')

                    if i[0][1]<minY :
                        global minY
                        minY = i[0][1]
                        #print ('minY')

            #print (minX)
            #print (maxX)
            imageTarWidth = (maxX-minX)
            #print (imageTarWidth)
            imageTarHeight = (maxY-minY)
            if(imageTarHeight<2*imageTarWidth):
                imageTarWidth = None
                imageTarHeight = None
                maxX = 0.0
                minX = 20000.0
                maxY = 0.0
                minY = 20000.0
                continue
            rectCenterX = (maxX + minX)/2
            rectCenterY = (maxY + minY)/2

            maxX = 0.0
            minX = 20000.0
            maxY = 0.0
            minY = 20000.0

            if imageTarWidth != None and imageTarWidth != -20000:
                cv2.drawContours(image, contours, count, (255,255,255), 20)
                processing(imageTarWidth, rectCenterX, rectCenterY)
                break


    cv2.imshow('Contours', image)

    cv2.imshow("Live Feed", frame)

    key = cv2.waitKey(10)
    if key == 27:
      cv2.destroyWindow("Live Feed")
      cv2.destroyWindow('Contours')
      cv2.destroyWindow('Threshed')
      break
