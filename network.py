import socket               # Import socket module
import threading

conn = None
soc = None
connected = False

class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print "Starting " + self.name
      startServer()
      print "Exiting " + self.name

def sendMessage( message): # send message to NTable client
        #receive = conn.recv(1024)
        #print(receive)
        conn.send(message + '\r\n')

def startServer():
    print ("here")
    while True:
        global conn
        print ("in loop")           # Now wait for client connection.
        conn, addr = soc.accept()
        global connected
        connected = True
        #sendMessage("Hi")
        #conn.send("Hi" + '\n')
        #receiveMessage( "Hi")    # Establish connection with client.
        #receive = conn.recv(1024)
        #if receive != None and receive != '' and receive != ' ':
            #print (receive)

global soc
soc = socket.socket()         # Create a socket object
host = "localhost" # Get local machine name
port = 3341                # Reserve a port for your service.
soc.bind((host, port))       # Bind to the port
soc.listen(5)
thread1 = myThread(1, "Thread-1", 1)
thread1.start()
print("send")
i = 0
while True:
    print(connected)
    if(connected):
        sendMessage("Hi")
    else:
        i = i + 1
    if i>10000000:
        break




#print ("Got connection from",addr)
#msg = conn.recv(1024)
#print (msg)
#if ( msg == "Hello Server" ):
#    print("Hii everyone")
#else:
#    print("Go away")
