from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password, check_password
from records.constants import special_charecters_list
from login.serializers import PersonSerializer
from login.models import Person
import json

# Create your views here.


@api_view(['GET'])
def login(request):

    dt={}
    for i in special_charecters_list:
        dt[i] = make_password(i) 

    data = json.dumps(dt)
    print(data)

    return Response(data)

@api_view(['GET'])
def get_data(request):
    items = Person.objects.all()
    serializer = PersonSerializer(items,many ="True")
    print(str(serializer))
    return Response(serializer.data)


@api_view(['POST'])
def add_user(request):
    """
    methord to add/create user in the data base
    """
    serializer = PersonSerializer(data = request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
       #print(serializer.data.name,serializer.data.user_name,serializer.data.password)
        return Response(serializer.errors)



#The json format 
"""
{
"first_name" : "Sathya",
"last_name" : "Sai",
"user_name" : "SSS",
"password" : "SSPN@515134",
"email" : "Sathya@gmail.com",
"contact_number"  : "5747385475",
"gender" : "Male",
"active_status" : 1,
"roll" : "admin",
"description" : "Test acc"
} 
"""