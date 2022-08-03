from django.urls import path
from Chat.views import *


urlpatterns = [
   
   path('chat', chat, name='blogs'),


]