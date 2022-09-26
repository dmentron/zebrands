from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import User

from applications.producto.models import Producto

# Create your models here.
class Usuario(TimeStampedModel):
    TIPO_USUARIO = (
        (1, 'ADNINISTRADOR'),
        (2, 'USUARIO SIMPLE')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.IntegerField(choices=TIPO_USUARIO)

    class Meta:
        db_table = 'usu_usuario'
        ordering = ['id']

    def __str__(self):
        return str(self.user.username) + '-' + str(self.tipo_usuario)

class NotificacionUsuario(TimeStampedModel):
    ACCION = (
        (1, 'CREA'),
        (2, 'ACTUALIZA'),
        (3, 'ELIMINA')
    )

    VISTA = (
        (0, 'NO'),
        (1, 'SI'),
    )
    id = models.AutoField('Key', primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.PROTECT)
    accion = models.IntegerField(choices=ACCION)
    vista = models.BooleanField('Notificación vista?', default=1, choices=VISTA)

    class Meta:
        db_table = 'usu_notificacion_usuario'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + '-' + str(self.producto.nombre)+ '-' + str(self.accion)+ '-' + str(self.user.username)

class SeguimientoUsuario(TimeStampedModel):
    ips = models.CharField('IPs del usuario', max_length=60, blank=True)
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.PROTECT)

    class Meta:
        db_table = 'usu_seguimiento_usuario'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + '-' + self.ips + '-' + str(self.producto)
