from django.shortcuts import render, redirect

# Create your views here.

def index_view(request):

    return redirect('/chat')

def chat_view(request):

    print("***** In HERE *****")

    return render(request, 'chat.html')
