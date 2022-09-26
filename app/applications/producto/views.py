from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    FormView,
    ListView,
    CreateView
)

from applications.producto.models import Producto

class ListProducts(TemplateView):
    template_name = 'producto/list_product.html'

class ListMarks(TemplateView):
    template_name = 'producto/list_mark.html'

class ListTypeProduct(TemplateView):
    template_name = 'producto/list_type_product.html'

