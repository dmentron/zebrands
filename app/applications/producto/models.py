from django.db import models
from ckeditor.fields import RichTextField
from model_utils.models import TimeStampedModel

# Create your models here.
class Marca(TimeStampedModel):

    MARCA_DELETED = (
        (1, 'SI'),
        (0, 'NO')
    )

    marca = models.CharField('Marca', null=True, max_length=80)
    activa = models.IntegerField('Marca Activa?', default=1, null=True, choices=MARCA_DELETED)

    class Meta:
        db_table = 'prod_marca'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + '-' + self.marca

class TipoProducto(TimeStampedModel):

    TIPO_DELETED = (
        (1, 'SI'),
        (0, 'NO')
    )

    nombre_tipo = models.CharField('Nombre Tipo', null=True, max_length=120)
    activa = models.IntegerField('Marca Activa?', default=1, null=True, choices=TIPO_DELETED)

    class Meta:
        db_table = 'prod_tipo_producto'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + '-' + self.nombre_tipo


class Producto(TimeStampedModel):
    sku = models.IntegerField('N° SKU')
    nombre = models.CharField('Nombre del producto', max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.FloatField('Precio')
    marca = models.ForeignKey(Marca, verbose_name='Marca', on_delete=models.PROTECT)
    tipo_producto = models.ForeignKey(TipoProducto, verbose_name='Tipo Producto', on_delete=models.PROTECT)
    stock = models.IntegerField('Stock')

    class Meta:
        db_table = 'prod_producto'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + '-' + str(self.sku) + '-' + self.nombre
   