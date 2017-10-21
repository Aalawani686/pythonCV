import socket               # Import socket module

soc = socket.socket()         # Create a socket object
host = "localhost" # Get local machine name
port = 3341                # Reserve a port for your service.
soc.bind((host, port))       # Bind to the port
soc.listen(5)                 # Now wait for client connection.
while True:
    conn, addr = soc.accept()     # Establish connection with client.
    print ("Got connection from",addr)
    msg = conn.recv(1024)
    print (msg)
    if ( msg == "Hello Server" ):
        print("Hi everyone")
    else:
        print("Go away")
