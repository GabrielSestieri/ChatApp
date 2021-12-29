import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050

def listen_for_messages_from_server(client):

    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~")[0]
            content = message.split("~")[1]

            print(f"[{username}] {content}")
        else:
            print("Message empty")

def send_message_to_server(client):

    while 1:

        message = input("\nMessage: ")
        if message != '':
            client.sendall(message.encode())
        else:
            print("Empty message")
            exit(0)

def communicate_to_server(client):

    username = input("Enter username: ")
    if username != '':
        client.sendall(username.encode())
    else:
        print("Username is required")
        exit(0)
    
    threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()

    send_message_to_server(client)

def main():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        client.connect((HOST, PORT))
        print("Successfully Connected to server")
    except:
        print("Unable to connect")

    communicate_to_server(client)

if __name__ == '__main__':
    main()





















