#import socket module
from socket import *
import sys # In order to terminate the program
MAX_SIZE_BYTES = 65535
serverSocket = socket(AF_INET, SOCK_STREAM)
port = 8080
hostname = 'localhost'
serverSocket.bind((hostname, port))
serverSocket.listen()

while True:
#Establish the connection
    print('Ready to serve... at 8080')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()
        print(outputdata)
#Send one HTTP header line into socket
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n\r\n")
#Fill in end
#Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
         # Send response message for file not found
        connectionSocket.send(b"HTTP/1.1 404 Not found\r\n\r\n")
        connectionSocket.send(b"<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")
        # Close the client socket
        connectionSocket.close()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data