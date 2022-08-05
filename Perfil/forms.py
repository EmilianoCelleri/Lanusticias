from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Perfil.models import Perfil


class UserEditForm(UserCreationForm):
    email=forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    first_name=forms.CharField(max_length=50, label='Nombre')
    last_name=forms.CharField(max_length=50, label='Apellido')

    class Meta:
        model = User
        fields= ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        
class AvatarForm(forms.Form):
    imagen=forms.ImageField(label='imagen')


class PerfilEditForm(UserCreationForm):
    web=forms.URLField(label='Mi web')
    descripcion=forms.CharField(max_length=200, label='Descripcion')

    class Meta:
        model = User
        fields= ['web', 'descripcion']