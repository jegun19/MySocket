import socket
import cv2

TCP_IP = "127.0.0.1"
TCP_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(1)

file = open('accept.mp4','wb')
conn, addr = s.accept()
print('Connection address: ', addr)
while 1:
    data = conn.recv(1048576)
    file.write(data)
    if not data: break

conn.close()

cap = cv2.VideoCapture('accept.mp4')

if(cap.isOpened() == False):
    print("Error opening")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        cv2.imshow('Frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    else:
        break


cap.release()
cv2.destroyAllWindows()