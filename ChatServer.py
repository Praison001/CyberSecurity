import socket

mysocket= socket.socket()
mysocket.bind(("0.0.0.0",1234))
mysocket.listen(1)
conn,add= mysocket.accept()
banner= "Connected"
conn.send(banner.encode())

while True:
    try:
        data=conn.recv(2048).decode()
        print("Received: ",data)
        if data == "exit":
            print("Closing")
            mysocket.close()
            break
        else:
            server= input("Send: ")
            conn.send(server.encode())
    except Exception as error:
        print("Error, closing")
        mysocket.close()
        
                      
