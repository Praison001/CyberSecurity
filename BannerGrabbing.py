import socket

target = input("Enter target: ")

while True:
    try:
        s= socket.socket()
        port= input("Enter port: ")
        if "exit" in port:
            break
        s.connect((target,int(port)))
        #s.send("Service \n".encode())
        s.send("GET / HTTP/1.0\n\n".encode())
        s.settimeout(4)
        ret=  s.recv(1024).decode()
        print(f"Service {ret}, port {port}")
        s.close()


    except Exception as error:
        print(error)

