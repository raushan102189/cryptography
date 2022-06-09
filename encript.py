import os
from cryptography.fernet import Fernet  
a = os.listdir()
file = input("file ")
with open(file,"rb")as rr:
    reading = rr.read()
key = Fernet.generate_key()
with open ("data.txt",'wb')as data:
    data.write(key)
newFile = "a"+file 
f = Fernet(key).encrypt(reading)
with open(newFile,"wb") as writeing:
    writeing.write(f)

secret = "rja"
# new = f.encrypt(reading)
print(f)

# z = Fernet(key).decrypt(f)
# print(z)
