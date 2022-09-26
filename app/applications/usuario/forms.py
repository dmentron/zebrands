# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username     = forms.CharField(widget=forms.DateInput(attrs={"class": "form-control", "placeholder": "Nombre usuario", "autofocus": "autofocus", "autocomplete":"off"},), required=True)
    password     = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Clave"},), required=False)

    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )

class UserForm(UserCreationForm):
    username   = forms.CharField(label="Usuario", widget=forms.TextInput(attrs={'class': 'form-control', 'v-model': 'username'}))
    first_name = forms.CharField(label="Nombres", widget=forms.TextInput(attrs={'class': 'form-control', 'v-model': 'first_name'}))
    last_name  = forms.CharField(label="Apellidos", widget=forms.TextInput(attrs={'class':'form-control', 'v-model': 'last_name'}))
    email      = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control', 'v-model': 'email'}))
    password  = forms.CharField(label="Contraseña", widget=forms.TextInput(attrs={'class': 'form-control', 'v-model': 'password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]