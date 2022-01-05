from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def registration_view(request):

    data = {
        "response": "Success"
    }

    return Response(data)