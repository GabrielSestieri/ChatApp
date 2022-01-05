from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def index_view(request):
    print("***** IN HERE *****")
    print(request.data)
    data = {
        "response": "Success"
    }
    return Response(data)

@api_view(['POST'])
def add_friend_view(request):

    data = {}

    return Response(data)