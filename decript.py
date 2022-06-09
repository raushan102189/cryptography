import os
from cryptography.fernet import Fernet  
a = os.listdir()
file = input("file ")
with open(file,"rb")as rr:
    reading = rr.read()
# key = Fernet.generate_key()
with open ("data.txt",'rb')as data:
    key =data.read()
newFile = "ab"+file 
f = Fernet(key).decrypt(reading)
with open(newFile,"wb") as writeing:
    writeing.write(f)