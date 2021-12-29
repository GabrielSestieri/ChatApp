import socket
import time
from datetime import *


PORT = 5051
SERVER = "192.168.1.31"
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT = "!DISCONNECT"

def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    return client


def start():
    connection = connect()
    while True:
        msg = connection.recv(1024).decode(FORMAT)
        print(msg)

start()