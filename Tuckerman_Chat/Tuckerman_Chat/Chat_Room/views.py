from django.shortcuts import render, redirect
import socket
import time
import threading


# Create your views here.

def index_view(request):

    return redirect('/chat')

def chat_view(request):
    print("***** In Chst View *****")


    PORT = 5051
    SERVER = "192.168.1.31"
    ADDR = (SERVER, PORT)
    FORMAT = "utf-8"
    DISCONNECT = "!DISCONNECT"

    def connect():
        print("***** IN CONNECT *****")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("***** AFTER CLIENT *****")
        client.connect(ADDR)
        print("***** AFTER CLIENT CONNECT *****")
        return client

    # def send(client, msg):
    #     client.send(msg.encode())

    def start():
        print("***** IN START *****")
        connected = False

        # answer = input("Connect to the server? (y/n) ")
        # if answer.lower() != "y":
        #     return

        print("***** BEFORE CONECTION *****")
        connection = connect()
        # username_status = False
        # while not username_status:
        #     username = input("Enter username: ")
        #     if username != '':
        #         send(connection, username)
        #         username_status = True
        #     else:
        #         print("Username is required")
        #         username_status = False
        print("***** BEFORE IF *****")
        if not connected:
            connected = True
            print("Connected To server")

        print("***** BEFORE THREAD *****")
        thread = threading.Thread(target=connect)
        thread.start()
            # msg = (input("Send a message: (q for quit): "))
            # if msg == "q":
            #     break
            # send(connection, msg)
        # send(connection, DISCONNECT)
        time.sleep(1)
        print("Disconnected")

    start()

    return render(request, 'chat.html')
