import socket
from threading import Thread, Lock
import time

class Client:

    PORT = 5051
    SERVER = "192.168.1.31"
    ADDR = (SERVER, PORT)
    FORMAT = "utf-8"
    DISCONNECT = "!DISCONNECT"

    def __init__(self, username, fullname):

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)
        self.username = username
        self.fullname = fullname
        self.messages = []
        self.send_message(username)
        time.sleep(1)
        self.send_message(fullname)
        receive_thread = Thread(target=self.receive_messages)
        receive_thread.start()
        self.lock= Lock()
    

    def receive_messages(self):
        while True:
            try: 
                msg = self.client.recv(1024).decode()

                self.lock.acquire()
                self.messages.append(msg)
                self.lock.release()
            except Exception as e:
                print("[ERROR]", e)
                break

    def send_message(self, msg):
        try:
            self.client.send(bytes(msg, "utf-8"))
            if msg == "{q}":
                self.client.close()
        except Exception as e:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(self.ADDR)
            print(e)
    
    def get_messages(self):
        messages_copy = self.messages[:]

        self.lock.acquire()
        self.messages = []
        self.lock.release()

        return messages_copy

    def diconnect(self):
        self.send_message("{q}")

    
















