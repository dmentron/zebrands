from ipaddress import ip_address
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, UpdateAPIView

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from applications.usuario.models import SeguimientoUsuario
from .serializer import SeguimientoSerializers, UserUpdateSerializers, UsersSerializers, UserCreateSerializers
from django.http import Http404

from django.contrib.auth.models import User

import socket

class UserListApiView(ListAPIView):
    # Here you get the list of all registred users
    serializer_class = UsersSerializers

    def get_queryset(self):
        object_user = User.objects.all()
        return object_user

class UserDetailApiView(ListAPIView):
    # Here you get the list of all registred users
    serializer_class = UsersSerializers

    def get_queryset(self):
        object_user = User.objects.filter(id=self.kwargs['pk'])
        return object_user

class UserCreateAPIView(CreateAPIView):
    # From here a user is created 
    authentication_classes = [TokenAuthentication]
    serializer_class = UserCreateSerializers

    def post(self, request, format=None):
        serializer = UserCreateSerializers(data=request.data)
        if serializer.is_valid():
            serializer.is_staff = True
            serializer.is_superuser = True
            serializer.save()

            #update hash password user
            # object_user = User.objects.filter(username=serializer.data['username'])
            # object_user.set_password(serializer.data['password'])
            # object_user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRetriveUpdateView(RetrieveUpdateAPIView):
    # From here a user is update 
    authentication_classes = [TokenAuthentication]
    serializer_class = UserUpdateSerializers
    queryset = User.objects.all()

class UserDeleteView(DestroyAPIView):
    # From here a user is delete 
    authentication_classes = [TokenAuthentication]
    serializer_class = UsersSerializers
    queryset = User.objects.all()

class UserAnonymousCreateAPIView(CreateAPIView):
    # From here a user  is created 
    authentication_classes = [TokenAuthentication]
    serializer_class = SeguimientoSerializers

    def post(self, request, format=None):
        serializer = SeguimientoSerializers(data=request.data)
        if serializer.is_valid():
            ip_address = socket.gethostbyname(socket.gethostname())
            print(ip_address)

            serializer.ips = ip_address
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UserAnonymousListApiView(ListAPIView):
    # Here you get the list of all registred users
    serializer_class = SeguimientoSerializers

    def get_queryset(self):
        object_seg = SeguimientoUsuario.objects.all()
        return object_seg     




