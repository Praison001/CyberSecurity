import hashlib
import os
rootdir = './Aratus/'

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        textfile= os.path.join(subdir, file)
        
        with open(textfile,"rb") as f:
            bytes = f.read() # read file as bytes
            readable_hash = hashlib.md5(bytes).hexdigest();
            if readable_hash!= "3b485abefcd07db1f3aa83b25b41e56f":
                print("Found a different hash!!!" + textfile + ":" + readable_hash + "<=== Better open this file and check what's up!")
            
            	
    
    