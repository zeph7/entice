# Entice

An Encrypted Chat Application developed in Python
 
![](https://www.pubnub.com/wp-content/uploads/2017/03/chat-app-in-terminal-with-python.png)


## What its for?

Here, I have developed an encrypted chat application so that 2 clients can chat with each other, thought a connection with server. But the server is unable to decypher the chat texts among the 2 clients. Its developed by the use of Socket Programming in Python, with encryption done by RSA Encryption ALgorithm.


## Requirments

Python 3 - version 3.6.5
### modules :
                  socket -> required for networking
                  threading -> required for simultaneous chatting 
                  tkinter -> required for GUI
                  random -> required for selection of random prime no. in RSA
                  time -> required to sleep the time
                  sys -> required for handling system exit
                  
       

## How to Use?

1. Firstly, run the server script (Server.py) on a system, to be made a server that is in connection with the 2 clients.
2. Secondly, run the first client script (client_1.py) on another system, here put the IP of the server that is shown on server console and alse put the Port of the server, that is fixed in the server script to 42000, finally enter your name, e.g.-Zephyr.
3. Then run the second client script (client_2.py) on different system, same here, put the Host IP, Port and your name.

Finally, connection is established now!!

You can chat with your friend with with one client as you and another client as your friend.
And without server interviewing your chats!!
Server script will show the encrypted messages shared among the 2 clients.


# Screenshots

## Server Sript :

![](https://github.com/ashish7zeph/Entice/blob/master/screenshot/img1.png)

## Client_1 Script : Zephyr

![](https://github.com/ashish7zeph/Entice/blob/master/screenshot/img2.png)

## Client_2 Script : Klaus

![](https://github.com/ashish7zeph/Entice/blob/master/screenshot/img3.png)

## Server after few conversation :

![](https://github.com/ashish7zeph/Entice/blob/master/screenshot/img4.png)


# Socket Programming

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server.
They are the real backbones behind web browsing. In simpler terms there is a server and a client. 
An example of sockect programming is given below.

![](https://xinyustudio.files.wordpress.com/2012/05/image_thumb.png?w=618&h=225)


# RSA (Rivest–Shamir–Adleman)

RSA (Rivest–Shamir–Adleman) is one of the first public-key cryptosystems and is widely used for secure data transmission. In such a cryptosystem, the encryption key is public and it is different from the decryption key which is kept secret (private). In RSA, this asymmetry is based on the practical difficulty of the factorization of the product of two large prime numbers, the "factoring problem". The acronym RSA is made of the initial letters of the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman, who first publicly described the algorithm in 1978. Clifford Cocks, an English mathematician working for the British intelligence agency Government Communications Headquarters (GCHQ), had developed an equivalent system in 1973, but this was not declassified until 1997.

![](https://s22908.pcdn.co/wp-content/uploads/2014/09/more-encrypted-chat-apps.jpg)

# Licence

Licensed under the MIT License
