# Entice Chat app

[![License](https://img.shields.io/github/license/ashish7zeph/Entice.svg?style=for-the-badge)](https://github.com/ashish7zeph/Entice/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/ashish7zeph/Entice.svg?style=for-the-badge)](https://github.com/ashish7zeph/Entice/graphs/contributors)
[![GitHub forks](https://img.shields.io/github/forks/ashish7zeph/Entice.svg?style=for-the-badge)](https://github.com/ashish7zeph/Entice/network/members)
[![GitHub stars](https://img.shields.io/github/stars/ashish7zeph/Entice.svg?colorB=green&style=for-the-badge)](https://github.com/ashish7zeph/Entice/stargazers)

[![Made with python](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Overview

An Encrypted Chat Application developed in Python

This is an encrypted chat application to make 2 clients offline chatting possible via LAN or Wifi hotspot, thought a connection with a system that is made as a server. 

The server is unable to decypher the chat texts among the 2 clients. It is developed by the use of Socket Programming in Python and the  encryption is done using RSA Encryption ALgorithm.

## Features

* Chatting
* Encryption
* Secure

## Requirments
```
Python 3 - version 3.6.5
```
### modules :

   * socket - Low-level networking interface
   * threading - Higher-level threading interface
   * tkinter - Python interface to the Tk GUI toolkit
   * random - Generate pseudo-random numbers
   * sys - System-specific parameters and functions
   * time - Time access and conversions

## Instructions

1. Clone or download the repo: `https://github.com/ashish7zeph/Entice`
2. Navigate to the folder `Entice`
3. Run the server script `Server.py` on a system to be made a server that is in connection with the 2 clients
4. Run the first client script `client_1.py` on another system
5. Put the IP of the server that is shown on server console in `client_1.py`
6. Put the Port of the server, that is fixed in the server script to 42000
7. Finally enter your name, e.g.-`Zephyr`
8. Then run the second client script `client_2.py` on different system
5. Put the IP and port of the server in `client_2.py` and enter your name e.g.-`klaus`

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

The code for creating a server socket in sockect programming used in this project is given below:

```python3
     HOST = gethostbyname(gethostname())     # get host IP
     PORT = 42000
     BUFFER_SIZE = 1024   # buffer size of receiver
     ADDRESS = (HOST, PORT)  # servers socket address

     SERVER = socket(AF_INET, SOCK_STREAM)   # create socket object
     SERVER.bind(ADDRESS)    # bind socket IP and port no.

     SERVER.listen(2)
     print('Server IP: ', HOST)
     print("Waiting for connection...")
     accept_incoming_connections()
     accept_incoming_connections()
```

The code for connecting a client socket with server socket in sockect programming used in this project is given below:

```python3
    HOST = input('Enter host: ')
    PORT = int(input('Enter port: '))
    NAME = input('Enter your name: ')
    BUFFER_SIZE = 1024
    ADDRESS = (HOST, PORT)

    CLIENT = socket(AF_INET, SOCK_STREAM)    # client socket object
    CLIENT.connect(ADDRESS) # to connect to the server socket address
```

# RSA (Rivest–Shamir–Adleman)

RSA (Rivest–Shamir–Adleman) is one of the first public-key cryptosystems and is widely used for secure data transmission. In such a cryptosystem, the encryption key is public and it is different from the decryption key which is kept secret (private). In RSA, this asymmetry is based on the practical difficulty of the factorization of the product of two large prime numbers, the "factoring problem". The acronym RSA is made of the initial letters of the surnames of Ron Rivest, Adi Shamir, and Leonard Adleman, who first publicly described the algorithm in 1978. Clifford Cocks, an English mathematician working for the British intelligence agency Government Communications Headquarters (GCHQ), had developed an equivalent system in 1973, but this was not declassified until 1997.

A key generation function code used in this project is given below:

```python3
    def key_generator():
    
        p, q = primes.choose_distinct_primes()
        n = p * q
        phi = (p-1) * (q-1)  # Euler's function (totient)
        e = choice(coprimes(phi))
        d = modinv(e, phi)
        
        public_key = [e, n]
        private_key = [d, n]
        return [public_key, private_key]
```

