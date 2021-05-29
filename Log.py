import datetime
log= []
def Log():
    global log
    now= datetime.datetime.today()
    string= input("Enter a log: ")
    log.append("{}.{}.{} :: {}.{} => {}".format(now.day,now.month,now.year,now.hour,now.minute,string))
    
def LogList():
    global log
    for one in log:
        print(one)
    
def Menu():
    while True:
        word= input("1.Write log\n2.See log\n3.Quit\n==>")
        if word =="1":
            Log()
        elif word =="2":
            LogList()
        elif word =="3":
            print("Bye")
            break
        else:
            print("Invalid")
            
if __name__=="__main__":
    Menu()


        
