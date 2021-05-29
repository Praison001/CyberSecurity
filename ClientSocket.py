import socket

mysocket= socket.socket()
mysocket.connect(("10.0.0.3",1234))
data= mysocket.recv(2048).decode()
print(data)
mysocket.close()
