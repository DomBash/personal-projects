#!/usr/bin/env python
# coding: utf-8

# In[6]:


import socket                                         

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = "127.0.0.1"                          
port = 9001                                           

serversocket.bind((host, port))                                  

serversocket.listen(2)  

myMsg = input()

client1,addr = serversocket.accept()
msg1 = client1.recv(1024) 
print("1st client connected")

client2,addr = serversocket.accept()
msg2 = client2.recv(1024)
print("2nd client connected")

nums = myMsg + " " + msg1.decode('ascii') + " " + msg2.decode('ascii') 

print(nums)
client1.send(nums.encode('ascii'))
client2.send(nums.encode('ascii'))

client1.close()
client2.close()

