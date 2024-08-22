from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import userSerializer
import random
# Create your views here.

@api_view(['POST'])
def register(request):
    user = userSerializer(data=request.data)

    if user.is_valid():
        user.save()
        return Response(data="success", status=200)
    else:

        return Response(data=user.errors, status=400)
    

@api_view(['POST'])
def mailuser(request):
    email = request.data['email']
    name = request.data['name']

    otp = ""

    for i in range(4):
        n = random.randrange(0,9)

        otp += str(n)