import socket
import sys

portNumber = 0
isInitialized = false
socket = None
connection = None

def __init__(self):
    global portNumber = 3341
    isInitialized = false


def startServer(): #startServer
    global socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    socket.bind((host, port))
    socket.listen(1)
    global connection, addr = socket.accept()


def waitForPing(): #wait for something to be sent
    if(socket != None):
        receive = socket.recv(1024)
        if receive == None or receive == ' ' :
            print ("Hasn't received ping")



def sendMessage(message): # send message to NTable client
    if(connection != None):
        onnection.send(message + "\n")
