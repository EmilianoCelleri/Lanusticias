from django.urls import path
from .views import *


urlpatterns = [
   
   path('editar_perfil', editar_perfil, name='editar_perfil'),
   path('agregar_avatar', agregar_avatar, name='agregar_avatar'),
   path('editar_informacion', editar_informacion, name='editar_informacion'),
   path('mostrar_perfil', mostrar_perfil, name='mostrar_perfil'),


]