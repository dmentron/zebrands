from django.contrib import admin

from applications.producto.models import Marca, TipoProducto, Producto

# Register your models here.
admin.site.register(Marca)
admin.site.register(TipoProducto)
admin.site.register(Producto)