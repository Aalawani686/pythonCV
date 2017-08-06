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
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        socket.bind((host, port))
        socket.listen(1)
        global connection
        connection, addr = socket.accept()
        isInitialized = True


    def waitForPing(self): #wait for something to be sent
        if(socket != None):
            receive = socket.recv(1024)
        if receive == None or receive == ' ' :
            print ("Hasn't received ping")



    def sendMessage(self, message): # send message to NTable client
        if(connection != None):
            connection.send(message + "\n")
