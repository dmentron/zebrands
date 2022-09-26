from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    FormView,
    ListView,
    CreateView
)
# Create your views here.

class IndexView(TemplateView):
    template_name = 'portal/index.html'