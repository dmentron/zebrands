from dataclasses import fields
from pyexpat import model
from rest_framework import serializers, pagination

from django.contrib.auth.models import User
from applications.producto.api.serializer import ProductoSerializers

from applications.usuario.models import SeguimientoUsuario

class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class UserCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        )

class UserUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

class SeguimientoSerializers(serializers.ModelSerializer):
    producto = ProductoSerializers()
    class Meta:
        model = SeguimientoUsuario
        fields = ('__all__')