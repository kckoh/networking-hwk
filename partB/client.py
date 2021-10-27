import socket
import sys

#create an INET, STREAMing socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print ('Failed to create socket')
	sys.exit()
print ('Socket connection established successfully')

host = '149.248.57.154'
port = 8080

s.connect((host , port))


#Send http messages
message = b"GET /index.html HTTP/1.1 \r\n\r\n"
try :
	#Set the whole string
	s.sendall(message)
except socket.error:
	#Send failed
	print ('Error occured')
	sys.exit()
print ('Message is sent successfully')

#Now receive data
reply = s.recv(4096)
print (reply.decode('utf-8'))
print("Exiting the program")
sys.exit()