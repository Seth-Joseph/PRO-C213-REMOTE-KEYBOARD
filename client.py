import socket
from threading import Thread

SERVER = None
PORT = 8000
IP_ADDRESS = '127.0.0.1'

def setup():
    global SERVER
    global IP_ADDRESS
    global PORT

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    print('\t\t\t\tConnected to server')

    musicWindow()
setup()