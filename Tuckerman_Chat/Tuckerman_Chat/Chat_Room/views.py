from django.shortcuts import render, redirect
import socket
import time
import threading
from .client import Client


# Create your views here.

def index_view(request):

    return redirect('/chat')

def chat_view(request):
    print("***** In Chat View *****")

    # user = Client("gabriel", "Gabriel Sestieri")
    # time.sleep(.1)
    # user.send_message(f"hello my name is {user.username}")
    # time.sleep(.1)
    # user.send_message(f"My full name is {user.fullname}")
    # time.sleep(.1)
    # user.send_message("hey everyone")
    # time.sleep(.1)
    # user.send_message("what yall doing?")
    # time.sleep(.1)
    # user.send_message("show me")
    # time.sleep(.1)
    # user.send_message("q")
    # time.sleep(.1)
    # user.send_message("bye")

    return render(request, 'chat.html')
