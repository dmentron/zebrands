from django.urls import path, re_path

from . import views


app_name = 'portal_app'

urlpatterns = [
    path('page/', views.IndexView.as_view(), name='page'),
]