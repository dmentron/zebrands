from django.urls import path, re_path

from applications.producto.api import api
from . import views


app_name = 'product_app'

urlpatterns = [

    path('list/product/', views.ListProducts.as_view(), name='list_product'),
    path('list/mark/', views.ListMarks.as_view(), name='list_mark'),
    path('list/type/product/', views.ListTypeProduct.as_view(), name='list_type_product'),


    #api marca
    path('api/list/marca/', api.MarcaListApiView.as_view(), name='api_list_marca'),
    path('api/create/marca/', api.MarcaCreateAPIView.as_view(), name='api_create_marca'),
    path('api/update/marca/<pk>/', api.MarcaRetriveUpdateView.as_view(), name='api_update_marca'),
    path('api/detail/marca/<pk>/', api.MarcaDetailApiView.as_view(), name='api_detail_marca'),
    path('api/remove/marca/<pk>/', api.MarcaDeleteView.as_view(), name='api_delete_marca'),


    #api tipo_producto
    path('api/list/tipo_producto/', api.TipoProductoListApiView.as_view(), name='api_list_tipo_producto'),
    path('api/create/tipo_producto/', api.TipoProductoCreateAPIView.as_view(), name='api_create_tipo_producto'),
    path('api/update/tipo_producto/<pk>/', api.TipoProductoRetriveUpdateView.as_view(), name='api_update_tipo_producto'),
    path('api/detail/tipo_producto/<pk>/', api.TipoProductoDetailApiView.as_view(), name='api_detail_tipo_producto'),
    path('api/remove/tipo_producto/<pk>/', api.TipoProductoDeleteView.as_view(), name='api_delete_tipo_producto'),

    #api producto
    path('api/list/producto/', api.ProductoListApiView.as_view(), name='api_list_producto'),
    path('api/create/producto/', api.ProductoCreateAPIView.as_view(), name='api_create_producto'),
    path('api/update/producto/<pk>/', api.ProductoRetriveUpdateView.as_view(), name='api_update_producto'),
    path('api/delete/producto/<pk>/', api.ProductoDeleteView.as_view(), name='api_delete_producto'),
    path('api/detail/producto/<pk>/', api.ProductoDetailApiView.as_view(), name='api_detail_producto'),

    #api seguimiento
    path('api/tracing/user/list/', api.SeguimientoUsuarioListApiView.as_view(), name='api_list_tracing_user_list'),
    path('api/tracing/user/create/', api.SeguimientoUsuarioCreateAPIView.as_view(), name='api_create_tracing_user_list'),
]