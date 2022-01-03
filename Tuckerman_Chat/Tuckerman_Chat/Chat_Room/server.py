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

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

clients = set()
clients_lock = threading.Lock()

def handle_client(connection, address):
    print(f"[NEW CONNECTION] {address} connected.")
    try:
        with clients_lock:
            for c in clients:
                ip = c.getpeername()[0]
                if ip == address[0]:
                    username = connection.recv(2048).decode('utf-8')
                    fullname = connection.recv(2048).decode('utf-8')
                    ACTIVE_CLIENTS[address[0]] = username, fullname
                    while True:
                        message = connection.recv(2048).decode("utf-8")
                        if not message:
                            break
                        if message == "q":
                            break
                        if message == "show me":
                            print(ACTIVE_CLIENTS)
                        for c in clients:
                            ip = c.getpeername()[0]
                            time = datetime.now().strftime("%H:%M")
                            if ip == address[0]:
                                print(f"[{time}] {username}: {message}")
                            else:
                                nip = str(ip)
                                print(f"{nip} has disconnected.")                   
    finally:
        with clients_lock:
            clients.remove(connection)
            print(f"{username} has disconnected")
        connection.close()
        

def start_server():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        connection, address = server.accept()
        with clients_lock:
            clients.add(connection)
            ACTIVE_CLIENTS[address[0]] = ""
        thread = threading.Thread(target=handle_client, args=(connection, address))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        
        
print("[STARTING] server is starting...")
start_server()
