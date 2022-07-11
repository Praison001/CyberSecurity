import sys
import socket

if len(sys.argv) == 2:
    print("Scanning the target IP...........")
    target_IP = socket.gethostbyname(sys.argv[1])
else:
    print("Usage: python3 PytPortScanner.py <Target IP>")

try:
    for port in range(1,65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection= s.connect_ex((target_IP,port))
        if connection == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exiting")
    sys.exit()
except socket.error:
    print("\n No response!")
    sys.exit()
except socket.gaierror:
    print("\n Cannot resolve hostname")
    sys.exit()
        
print("DONE!!!!")
