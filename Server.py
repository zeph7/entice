"""Server Script for multithreaded chat application for two clients"""
from socket import *
from threading import Thread


client_sock = []    # stores both client sockets
client_addresses = {}   # stores {key: client socket, values: client address}
public_key = []     # stores public keys of both clients


def accept_incoming_connections():
    """Sets up handling for incoming clients"""
    client, client_address = SERVER.accept()
    client_sock.append(client)
    print("%s:%s has connected." % client_address)
    public_key.append(client.recv(BUFFER_SIZE))
    client_addresses[client] = client_address


def handle_client1(client_sock, client_addresses):
    """Handles a first client connection"""
    client_sock[0].send(public_key[1])
    
    while True:
        msg0 = client_sock[0].recv(BUFFER_SIZE)
        client_sock[1].send(msg0)
        print(" Client 1: %s" % msg0.decode('utf8'))


def handle_client2(client_sock, client_addresses):
    """Handles a second client connection"""
    client_sock[1].send(public_key[0])
    
    while True:
        msg1 = client_sock[1].recv(BUFFER_SIZE)
        client_sock[0].send(msg1)
        print(" Client 2: %s" % msg1.decode('utf8'))


#----SOCKET Part----
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

Thread(target = handle_client1, args = (client_sock, client_addresses)).start()
Thread(target = handle_client2, args = (client_sock, client_addresses)).start()
print('Encrypted conversation: ')
SERVER.close()
