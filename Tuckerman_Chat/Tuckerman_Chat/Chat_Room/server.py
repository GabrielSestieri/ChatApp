import socket
import threading
from datetime import datetime

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
LISTENER_LIMIT = 5
active_clients = []

def listen_for_messages(client, username):

    while 1:

        message = client.recv(2048).decode('utf-8')
        print("Message: " + message)
        if message != '':
            final_msg = username + '~' + message
            print("Final Message: " + final_msg)
            send_message_to_all(final_msg)

        else:
            print("Message is empty")

def send_message_to_client(client, message):
    print("***** In Send Message to Client *****")

    client.sendall(message.encode())

def send_message_to_all(message):
    print("***** In Send Message To All *****")

    for user in active_clients:
        print("***** Sending Message to User *****")
        send_message_to_client(user[1], message)

def client_handler(client):

    while 1:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            break
        else:
            print("Username is empty")

    threading.Thread(target=listen_for_messages, args=(client, username)).start()

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server.bind((HOST, PORT))
        print(f"Running Server on: {HOST} : {PORT}")

    except:
        print("Unable to bind host")

    server.listen(LISTENER_LIMIT)
    while 1:

        client, address = server.accept()

        print(f"Successfully connected to {address[0]} : {address[1]}")

        threading.Thread(target=client_handler, args=(client, )).start()

if __name__ == '__main__':
    main()

    


