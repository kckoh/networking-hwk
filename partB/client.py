import socket
import requests

HOST = ''    # The host IP address
PORT = 80              # host port number
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
message = ''    #message sent to the server to get HTML file
s.send(message.encode())

#print data received from the server
data = s.recv(1024)
while data:
    data = s.recv(1024)
    print('Received:' + data.decode())
s.close()