from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, UpdateAPIView

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from applications.producto.models import Marca, Producto, TipoProducto
from django.contrib.auth.models import User
from applications.producto.utils.functions import notification

from applications.usuario.models import NotificacionUsuario, SeguimientoUsuario
from .serializer import (
    CreateProductoSerializers, 
    MarcaSerializers, 
    ProductoUpdateSerializers, 
    SeguimientoUsuarioSerializers, 
    TipoProductoSerializers, 
    ProductoSerializers
)
from django.http import Http404

import socket

""" CRUD MARCA """
class MarcaListApiView(ListAPIView):
    # Here you get the list of all registred marcas
    serializer_class = MarcaSerializers

    def get_queryset(self):
        object_user = Marca.objects.filter(activa=1)
        return object_user

class MarcaDetailApiView(ListAPIView):
    # Here you get the list of all registred users
    serializer_class = MarcaSerializers

    def get_queryset(self):
        object_marca = Marca.objects.filter(id=self.kwargs['pk'])
        return object_marca

class MarcaCreateAPIView(CreateAPIView):
    # From here a marcas is created 
    authentication_classes = [TokenAuthentication]
    serializer_class = MarcaSerializers

    def post(self, request, format=None):
        serializer = MarcaSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MarcaRetriveUpdateView(RetrieveUpdateAPIView):
    # From here a marcas is update 
    authentication_classes = [TokenAuthentication]
    serializer_class = MarcaSerializers
    queryset = Marca.objects.all()

class MarcaDeleteView(RetrieveUpdateAPIView):
    # From here a marcas is delete 
    authentication_classes = [TokenAuthentication]
    serializer_class = MarcaSerializers
    queryset = Marca.objects.all()



""" CRUD TIPO PRODUCTO """
class TipoProductoListApiView(ListAPIView):
    # Here you get the list of all registred tipo_producto
    serializer_class = TipoProductoSerializers

    def get_queryset(self):
        object_tipo_producto = TipoProducto.objects.filter(activa=1)
        return object_tipo_producto

class TipoProductoDetailApiView(ListAPIView):
    # Here you get the list of all registred users
    serializer_class = TipoProductoSerializers

    def get_queryset(self):
        object_type = TipoProducto.objects.filter(id=self.kwargs['pk'])
        return object_type

class TipoProductoCreateAPIView(CreateAPIView):
    # From here a tipo_producto is created 
    authentication_classes = [TokenAuthentication]
    serializer_class = TipoProductoSerializers

    def post(self, request, format=None):
        serializer = TipoProductoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TipoProductoRetriveUpdateView(RetrieveUpdateAPIView):
    # From here a tipo_producto is update 
    serializer_class = TipoProductoSerializers
    queryset = TipoProducto.objects.all()

class TipoProductoDeleteView(RetrieveUpdateAPIView):
    # From here a marcas is delete 
    authentication_classes = [TokenAuthentication]
    serializer_class = TipoProductoSerializers
    queryset = TipoProducto.objects.all()

""" CRUD PRODUCTO """
class ProductoListApiView(ListAPIView):
    # Here you get the list of all registred tipo_producto
    serializer_class = ProductoSerializers

    def get_queryset(self):
        object_producto = Producto.objects.all()
        return object_producto

class ProductoDetailApiView(ListAPIView):
    # Here you get the list of all registred users
    serializer_class = ProductoSerializers

    def get_queryset(self):
        object_producto = Producto.objects.filter(id=self.kwargs['pk'])
        return object_producto

class ProductoCreateAPIView(CreateAPIView):
    # From here a tipo_producto is created 
    authentication_classes = [TokenAuthentication]
    serializer_class = CreateProductoSerializers

    def post(self, request, format=None):
        serializer = CreateProductoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoRetriveUpdateView(UpdateAPIView):
    # From here a tipo_producto is update 
    authentication_classes = [TokenAuthentication]
    serializer_class = ProductoUpdateSerializers

    def get_queryset(self, pk):
        return Producto.objects.filter(id = pk).first()

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            producto_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if producto_serializer.is_valid():
                producto_serializer.save()

                # Here the notification will be generated, where it is saved in a table and mail is sent
                notification(pk, 2)

                return Response(producto_serializer.data, status=status.HTTP_200_OK)
            return Response(producto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductoDeleteView(DestroyAPIView):
    # From here a tipo_producto is delete 
    authentication_classes = [TokenAuthentication]
    serializer_class = ProductoSerializers
    queryset = Producto.objects.all()

""" Seguimiento """

class SeguimientoUsuarioListApiView(ListAPIView):
    # Here you get the list of all registred marcas
    serializer_class = SeguimientoUsuarioSerializers

    def get_queryset(self):
        object_seguimiento = SeguimientoUsuario.objects.all()
        return object_seguimiento

class SeguimientoUsuarioCreateAPIView(CreateAPIView):
    # From here a marcas is created 
    serializer_class = SeguimientoUsuarioSerializers

    def post(self, request, format=None):
        serializer = SeguimientoUsuarioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)