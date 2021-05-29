import socket

host="0.0.0.0"
port= 1234
buffer=1000

mysocket=socket.socket()
mysocket.bind((host,port))
mysocket.listen(1)
print("Listening on {port}...")

conn,add= mysocket.accept()

print("Connected")

while True:
    command= input("Enter command: ")
    conn.send(command.encode())
    if command.lower=="exit":
        break
    results= conn.recv(buffer).decode()
    print(results)


conn.close()
mysocket.close()

