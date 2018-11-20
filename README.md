# Entice
An Encrypted Chat Application developed in Python


## What its for?

Here, I have developed an encrypted chat application so that 2 clients can chat with each other, thought a connection with server. But the server is unable to decypher the chat texts among the 2 clients. Its developed by the use of Socket Programming in Python, with encryption done by RSA Encryption ALgorithm.


## Requirments

Python 3 - version 3.6.5
  ### module - 
                  socket: required for networking
                  threading: required for simultaneous chatting 
                  tkinter: required for GUI
                  random: required for selection of random prime no. in RSA
                  time: required to sleep the time
                  sys: required for handling system exit
       

## How to Use?

1. Firstly, run the server script (Server.py) on a system, to be made a server that is in connection with the 2 clients.
2. Secondly, run the first client script (client_1.py) on another system, her put the IP of the server that is shown on server console and alse put the Port of the server, that is fixed in the server script to 42000, finally enter your name.
3. Then run the second client script (client_2.py) on different system, same here, put the Host IP, Port and your name.

Finally, connection is established now!!

You can chat with your friend with with one client as you and another client as your friend.
And without server interviewing your chats!!
Server script will show the encrypted messages shared among the 2 clients.


## Screenshots

**Server Sript

![](https://github.com/ashish7zeph/Entice/blob/master/screenshot/img1.png)

**Clinet 1

![](https://github.com/ashish7zeph/Entice/blob/master/screenshot/img12.png)

**Client 2

![](https://github.com/ashish7zeph/Entice/blob/master/screenshot/img3.png)


**Server after few conversation

![](https://github.com/ashish7zeph/Entice/blob/master/screenshot/img4.png)


# Licence

Licensed under the MIT License
