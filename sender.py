import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005


file = open(r'/home/jeffrey/demovid4.mp4','rb')
data = file.read()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.sendall(data)

s.close()

