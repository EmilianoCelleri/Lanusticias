from django.urls import path
from .views import editar_perfil


urlpatterns = [
   
   path('editar_perfil', editar_perfil, name='editar_perfil'),


]