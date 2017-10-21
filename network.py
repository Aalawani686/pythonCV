import socket
import sys
import threading

class Network(object):



    portNumber = 0
    isInitialized = False
    s = None
    connection = None


    class myThread (threading.Thread):
        def __init__(self, threadID, name, counter):
            threading.Thread.__init__(self)
            self.threadID = threadID
            self.name = name
            self.counter = counter

        def run(self):
            print ("Starting " + self.name)
            Network.startServer()
            print ("Exiting " + self.name)


    def __init__(self):
        global portNumber
        portNumber = 3341
        global isInitialized
        isInitialized = False

    def userServer(self):
        global s


        thread1 = self.myThread(1, "Thread-1", 1)
        thread1.start()
        print("thread started")

    def startServer(): #startServer

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = "localhost"
        s.bind((host, portNumber))

        global connection
        print ("in startServer")
        s.listen(5)
        while True:

            connection, addr = s.accept()
            print ("accepted")
            global isInitialized
            isInitialized = True
            connection.sendMessage("hi")


    def waitForPing(self): #wait for something to be sent
        if(s != None):
            receive = s.recv(1024)
        if receive == None or receive == ' ' :
            print ("Hasn't received ping")



    def sendMessage(self, message): # send message to NTable client
        if(isInitialized !=  False):
            connection.send(message + "\n")
