#import socket module
import socket
import sys

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Prepare a server socket
PORT = 12000
HOST = socket.gethostbyname(socket.gethostname())
serverSocket.bind((HOST, PORT))
serverSocket.listen(5)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        # Close the client connection socket
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send(b"HTTP/1.1 404 Not found\r\n\r\n")
        connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
        # Close the client socket
        connectionSocket.close()
    
serverSocket.close()
sys.exit()
