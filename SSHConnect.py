from sys import stderr
import paramiko

ssh= paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
target= input("Enter target IP: ")
port= 22
user= "msfadmin"
passwd= "msfadmin"

ssh.connect(hostname= target, username=user, password= passwd)

stdin, stdout, stderr= ssh.exec_command('ifconfig')

print(f"Data is: {stdout.read().decode()} \n Errors: {stderr.read().decode()}")