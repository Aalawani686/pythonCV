import numpy as np
import cv2
import math
import socket
import sys


class Network(object):

    import socket
    import sys

    portNumber = 0
    isInitialized = False
    socket = None
    connection = None

    def __init__(self):
        global portNumber
        portNumber = 3341
        isInitialized = False


    def startServer(self): #startServer
        global socket
        socket = socket.socket()         # Create a socket object
        host = "localhost" # Get local machine name
        port = 3341                # Reserve a port for your service.
        socket.bind((host, port))       # Bind to the port
        socket.listen(5)
        global connection                # Now wait for client connection.
        connection, addr = socket.accept()


    def waitForPing(self): #wait for something to be sent
        if(socket != None):
            receive = connection.recv(1024)
        if receive == None or receive == ' ' :
            print ("Hasn't received ping")



    def sendMessage(self, message): # send message to NTable client
        connection.send(message + '/n')


#Video_capture = cv2.VideoCapture(1)
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
    return math.atan(dy1/dx1)-math.atan(dy2/dx2);

def processing(imageTarWidth, rectCenterX, rectCenterY):

        if imageTarWidth != None :
            #print(imageTarWidth)
            distance  = targetWidth * focalLength / imageTarWidth

            offsetX = abs(rectCenterX - horizCenter)
            offsetY = abs(rectCenterY - vertiCenter)

            azimuth = np.arctan(offsetX/ focalLength)*180/math.pi
            altitude = np.arctan(offsetY/ focalLength)*180/math.pi
            #print ('Distance' + str(distance))
            #print ('Azimuth' + str(azimuth))
            #print ('Altitude' + str(altitude))

            #network.sendMessage(str(distance))
            #network.sendMessage(str(azimuth))
            #network.sendMessage(str(altitude))

            imageTarWidth = None
            imageTarHeight = None
            rectCenterX = None
            rectCenterY = None

#def __init__(self):
network = Network()
network.startServer()
network.waitForPing()

while(True):
    print('before message')
    network.sendMessage("Does this work?")
    print('sent')
