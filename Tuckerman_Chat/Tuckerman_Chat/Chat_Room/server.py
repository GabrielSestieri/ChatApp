import socket
import threading
import time
from datetime import *


PORT = 5051
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT = "!DISCONNECT"
ACTIVE_CLIENTS = {}
username_status = False
username = ""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()

def handle_client(connection, address):
    global username_status
    print(f"[NEW CONNECTION] {address} connected.")

    try:
        connected = True
        while connected:
            while not username_status:
                username = connection.recv(2048).decode('utf-8')
                if username != '':
                    ACTIVE_CLIENTS[address[0]] = username
                    username_status = True
                    break
                else:
                    print("Username is empty")
                    
            msg = connection.recv(2048).decode(FORMAT)
            if not msg:
                break
            if msg == DISCONNECT:
                connected = False
            print(f"[{address}] {msg}")
            index = 0
            with clients_lock:
                for c in clients:
                    time = datetime.now().strftime("%H:%M")
                    c.sendall(f"\n[{ACTIVE_CLIENTS[address[0]]}, {time}] {msg}".encode(FORMAT))
                    index += 1
                    
    finally:
        with clients_lock:
            clients.remove(connection)

        connection.close()
         
        

def start_server():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        connection, address = server.accept()
        print(connection)
        print(address)
        with clients_lock:
            clients.add(connection)
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        connection.send(f"Welcome to the server {address[0]}! \n".encode(FORMAT))
        connection.send(f"Enter !DISCONNECT to exit the server.".encode(FORMAT))
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        
        
print("[STARTING] server is starting...")
start_server()
