import socket
import sys
import threading

class Network(object):

    sendDistance = None
    sendAzimuth = None
    sendAltitude = None

    portNumber = 0
    isInitialized = False
    s = None
    connection = None


    class myThread (threading.Thread):
        network = None
        def __init__(self, threadID, name, counter, network):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter
            self.network = network

        def run(self):
            print ("Starting " + self.name)
            Network.startServer(self.network)
            print ("Exiting " + self.name)

    def setDistance(self, message):
        self.sendDistance = message
        #print (self.sendString)

    def setAzimuth(self, message):
        self.sendAzimuth = message
        #print (self.sendString)

    def setAltitude(self, message):
        self.sendAltitude = message
        #print (self.sendString)

    def waitForPing(self): #wait for something to be sent
        if(s != None):
            receive = s.recv(1024)
        if receive == None or receive == ' ' :
            print ("Hasn't received ping")

    def sendMessage(self, message): # send message to NTable client
        if(isInitialized !=  False):
            connection.send(message + b'\n')

    def __init__(self):
        global portNumber
        portNumber = 3341
        global isInitialized
        isInitialized = False

    def userServer(self):
        global s


        thread1 = self.myThread(1, "Thread-1", 1, self)
        thread1.start()
        print("thread started")

    def startServer(self): #startServer

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "localhost"
        s.bind((host, portNumber))

        global connection
        print ("in startServer")
        s.listen(5)
        #while True:

        connection, addr = s.accept()
        print ("accepted")
        global isInitialized
        isInitialized = True

        while True:
            if(self.sendDistance!=None):

                self.sendMessage(b"Distance: " + self.sendDistance.encode('utf-8'))
                self.sendDistance = None

            if(self.sendAzimuth!=None):

                self.sendMessage(b"Azimuth: " + self.sendAzimuth.encode('utf-8'))
                self.sendAzimuth = None

            if(self.sendAltitude!=None):

                self.sendMessage(b"Altitude: " + self.sendAltitude.encode('utf-8'))
                self.sendAltitude = None
