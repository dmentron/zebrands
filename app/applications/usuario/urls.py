from django.urls import path, re_path

from applications.usuario.api import api
from . import views


app_name = 'user_app'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('control-panel/', views.ControlPanelView.as_view(), name='control_panel'),
    path('list-user/', views.ListUsers.as_view(), name='list_user'),
    path('user/anonymus/', views.UserAnonymusView.as_view(), name='user_anonymus'),

    #api
    path('api/list/user/', api.UserListApiView.as_view(), name='api_list_user'),
    path('api/create/user/', api.UserCreateAPIView.as_view(), name='create_user'),
    path('api/update/user/<pk>/', api.UserRetriveUpdateView.as_view(), name='update_user'),
    path('api/detail/user/<pk>/', api.UserDetailApiView.as_view(), name='detail_user'),
    path('api/delete/user/<pk>/', api.UserDeleteView.as_view(), name='delete_user'),

    path('api/capture/data/', api.UserAnonymousCreateAPIView.as_view(), name='capture_data'),
    path('api/list/capture/data/', api.UserAnonymousListApiView.as_view(), name='list_capture_data'),
]