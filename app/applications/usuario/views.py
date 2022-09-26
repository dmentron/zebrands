from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    FormView,
    ListView,
    CreateView
)


from applications.usuario.forms import LoginForm, UserForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# 
def index(request):
    # function for login page
    data = {
        'form': LoginForm,
    }
    return render(request, 'usuario/login.html', data)

def user_access(request):
    # function that generates the user's login and creates a session

    username = request.POST['username']
    password = request.POST['password']

    request.session['error'] = None

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            request.session['dic_usuario'] = {
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_staff': user.is_staff,
            }

            return redirect('user_app:control_panel')
        else:
            mensaje = 'El usuario no esta activo, porfavor comunicarse con el administrador'
            error = True
    else:
        mensaje = 'El usuario no existe'
        error = True

    request.session['error'] = error
    request.session['mensaje'] = mensaje

    return redirect('index')

# area of view
class ControlPanelView(TemplateView):
    template_name = 'control_panel.html'
    

class ListUsers(FormView):
    template_name = 'usuario/list_user.html'
    form_class = UserForm

    def get_queryset(self):
        object_list = User.objects.all()
        return object_list

class UserAnonymusView(TemplateView):
    template_name = 'usuario/user_anonymus.html'


















