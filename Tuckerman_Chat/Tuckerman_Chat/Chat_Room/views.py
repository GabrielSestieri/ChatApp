from django.shortcuts import render

# Create your views here.

def chat_view(request):

    print("***** In HERE *****")

    return render(request, 'chat.html')
