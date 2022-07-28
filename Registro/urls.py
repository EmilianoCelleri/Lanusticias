from django.urls import path
from Registro.views import register


urlpatterns = [
   
    path('registro/', register, name="registro"),

    


]