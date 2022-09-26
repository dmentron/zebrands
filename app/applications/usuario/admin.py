from django.contrib import admin

from applications.usuario.models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(NotificacionUsuario)
admin.site.register(SeguimientoUsuario)
