import socket


mysocket= socket.socket()
mysocket.bind(("0.0.0.0",1234))
mysocket.listen(5)    #how much connections
conn,add= mysocket.accept()
buffer=2048
data=b""
while True:
    packet= conn.recv(buffer)
    parsed= packet.decode()
    data+=packet
    print(parsed)
    if len(packet)<buffer:
        print("within limit")

    


