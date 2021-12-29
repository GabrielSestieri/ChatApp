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
USERNAME_STATUS = {}
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
            with clients_lock:
                for c in clients:
                    ip = c.getpeername()[0]

                    if ip == address[0]:
                        if USERNAME_STATUS[ip] == False:
                            username = connection.recv(2048).decode('utf-8')
                            if username != '':
                                ACTIVE_CLIENTS[address[0]] = username
                                username_status = True
                                USERNAME_STATUS[ip] = True
                                break
                            else:
                                print("Username is empty")
                        else:
                            break
            msg = connection.recv(2048).decode(FORMAT)
            if not msg:
                break
            if msg == DISCONNECT:
                connected = False
            print(f"[{address}] {msg}")
            print(ACTIVE_CLIENTS)
            with clients_lock:
                for c in clients:
                    ip = c.getpeername()[0]
                    time = datetime.now().strftime("%H:%M")
                    c.sendall(f"\n[{ACTIVE_CLIENTS[ip]}, {time}] {msg}".encode(FORMAT))
            
                
                        
    finally:
        with clients_lock:
            clients.remove(connection)

        connection.close()
        
         
        

def start_server():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        connection, address = server.accept()
        with clients_lock:
            clients.add(connection)
            ACTIVE_CLIENTS[address[0]] = ""
            USERNAME_STATUS[address[0]] = False
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        connection.send(f"Welcome to the server {address[0]}! \n".encode(FORMAT))
        connection.send(f"Enter !DISCONNECT to exit the server.".encode(FORMAT))
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        
        
print("[STARTING] server is starting...")
start_server()
