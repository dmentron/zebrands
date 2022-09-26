from rest_framework import serializers

from applications.producto.models import Marca, TipoProducto, Producto
from applications.usuario.models import SeguimientoUsuario

class MarcaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('__all__')

class TipoProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = ('__all__')

class ProductoSerializers(serializers.ModelSerializer):
    marca = MarcaSerializers()
    tipo_producto = TipoProductoSerializers()
    class Meta:
        model = Producto
        fields = ('__all__')

class CreateProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            'sku',
            'nombre',
            'precio',
            'stock',
            'marca',
            'tipo_producto',
            'descripcion'
        )

class ProductoUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            'nombre',
            'precio',
            'stock',
            'descripcion'
        )

class SeguimientoUsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = SeguimientoUsuario
        fields = ('__all__')

