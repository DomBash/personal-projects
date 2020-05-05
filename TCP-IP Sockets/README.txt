Write a program (language of your choosing) that is run separately by three machines (with hardcoded IP addresses, e.g. 127.0.0.1) each of which inputs an integer on the command line. This program should send that integer to the other two machines, and receive an integer from the other two machines. Finally, all three integers (including your own) should be printed to terminal. The communication should be sent/received using TCP/IP sockets provided by the OS (Linux/Mac/Windows).


Coding Challenge #2:
I chose to do coding challenge #2 in python. I have attached a file for a server and a client.
Steps for running:
Start SocketServer.py and input integer
Start SocketClient.py and input integer
Start second instance of SocketClient.py and input integer