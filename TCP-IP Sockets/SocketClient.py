#!/usr/bin/env python
# coding: utf-8

# In[3]:


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

host = "127.0.0.1"                           
port = 9001

myMsg = input()

s.connect((host, port))                               
s.send(myMsg.encode('ascii'))

msg = s.recv(1024)  
print (msg.decode('ascii'))

s.close()

