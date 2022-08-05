from django.urls import path
from Chat.views import *


urlpatterns = [
   
   path('chat', chat, name='chat'),
   #path('mandar_mensaje', mandar_mensaje, name='mandar_mensaje'),
   path('chat/mandar_mensaje', MandarMensaje.as_view(), name='mandar_mensaje'),
   path('mensajes/<id>', mensajes, name='mensajes'),


]