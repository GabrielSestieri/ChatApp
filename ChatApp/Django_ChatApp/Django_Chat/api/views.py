from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import *
import random


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

@api_view(['POST'])
def login_user(request):

    data={}

    randNum = 0
    anonName = ""

    randNum = random.randint(0, 100000000)

    print("***** DATA BELOW *****")
    print(request.data['isAnonymus'])
    print(request.data['uID'])
    data['response'] = "Success!"

    if (request.data['isAnonymus']):
        anonName = "Anon" + str(randNum)
        sameName = True
        while sameName:
            foundName = False
            for user in User.objects.all():
                if user.displayName == anonName:
                    randNum = random.randint(0, 100000000)
                    anonName = "Anon" + str(randNum)
                    foundName = True
                    break
            if not foundName:
                sameName = False

        User.objects.create(displayName=anonName, uID=request.data['uID'])
        data['displayName'] = anonName
        return Response(data)
    else:
        newUser = User.objects.create(displayName=request.data['displayName'], email=request.data['email'], uID=request.data['uID'])
        data['displayName'] = newUser.displayName
        return Response(data)