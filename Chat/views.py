from django.shortcuts import render
from .models import Mensaje

# Create your views here.


def chat(request):

    mensajes=Mensaje.objects.filter(receptor_id=request.user.id)

    return render (request, 'chat.html', {'mensajes':mensajes})