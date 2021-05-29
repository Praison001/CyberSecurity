import socket

mysocket= socket.socket()

ip= input("Enter IP to connect: ")
port= input("Enter the port to connect: ")

mysocket.connect(ip,port)

while True:
    try:
        data= mysocket.recv(2048).decode()
        print("Received: ",data)
        client= input("Send: ")
        if client =="exit":
            mysocket.send(client.encode())
            print("Connection Terminated")
            mysocket.close()
            break
        else:
            mysocket.send(client.encode())

    except Exception as error:
        print("Error Occured")
        mysocket.close()
