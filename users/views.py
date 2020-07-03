from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

import requests, json
from users.models import Users

from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.serializers import UsersSerializer, AddressSerializer, CompanySerializer, GeoSerializer

# Create your views here.
# show all routes
@api_view(['GET'])
def showRoutes(request):
    data = {
        "/": "show all routes",
        "users": "show all users",
        "users/id": "show user with particular id",
        "delete": "delete all users",
        "delete/id": "delete a particular user",
        "delete/username": "delete a particular user",
        "create": "create a user",

    }
    return Response(data)


# get all users here
@api_view(['GET'])
def getUsers(request):
    response = requests.get(url)
    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)


# # get user by id
@api_view(['GET'])
def getUserByid(request, userId):
    users = Users.objects.get(id=userId)
    serializer = UsersSerializer(users, many=False)
    return Response(serializer.data)


# get user by username
@api_view(['GET'])
def getUserByUsername(request, username):
    users = Users.objects.get(username=username)
    serializer = UsersSerializer(users, many=False)
    return Response(serializer.data)

# delete a user with particular id
@api_view(['DELETE'])
def delete_user(request, id):
    Users.objects.filter(id=id).delete()
    return HttpResponse('data removed successfully!')


#delete all users
def deleteAll(request):
    Users.objects.all().delete()
    return HttpResponse('all users removed successfully!')


# create a user
@api_view(['POST'])
def addUser(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else :
        print("saving error")
    return redirect('/users')


