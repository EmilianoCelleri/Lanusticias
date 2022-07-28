from tabnanny import verbose
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Editar_perfil(UserCreationForm):
    email=forms.EmailField()
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)
    first_name=forms.CharField(max_length=50, label='Nombre')
    last_name=forms.CharField(max_length=50, label='Apellido')
    descripcion= forms.CharField(max_length=150, label='Descripcion')
    web=forms.URLField(max_length=50, label='Mi pagina web')

    class Meta:
        model = User
        fields= ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'descripcion', 'web']
        