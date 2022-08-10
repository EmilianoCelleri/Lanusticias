from urllib import request
from django.shortcuts import render
from .models import Mensaje

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

@login_required
def chat(request):

    mensajes=Mensaje.objects.filter(receptor_id=request.user.id)
    mensajes_enviados=Mensaje.objects.filter(emisor_id=request.user.id)
    return render (request, 'chat.html', {'mensajes':mensajes,'mensajes_enviados':mensajes_enviados})

class MandarMensaje(CreateView, LoginRequiredMixin):
    model = Mensaje
    template_name="mensaje_form.html"
    success_url = reverse_lazy('chat')
    fields = ['cuerpo','receptor']

    def form_valid(self, form):
        """Forzar el usuario emisor a Request.user"""
        self.mensaje = form.save(commit=False)
        self.mensaje.emisor_id = self.request.user.id
        self.mensaje.save()

        return super(MandarMensaje, self).form_valid(form)
    

@login_required
def mensajes(request,id):
    
    mensaje=Mensaje.objects.get(id=id)
    '''Traigo un objeto, si el mensaje lo mande yo soy el emisor, si lo recibi soy el receptor'''
    if mensaje.emisor == request.user:
        yo=mensaje.emisor
        otro=mensaje.receptor
        nombre=mensaje.receptor
    else:
        yo=mensaje.receptor
        otro=mensaje.emisor
        nombre=mensaje.emisor
    
    
    mensajes_enviados=Mensaje.objects.filter(receptor=otro).filter(emisor=yo)
    mensajes_recibidos=Mensaje.objects.filter(receptor=yo).filter(emisor_id=otro)    
    
    return render (request, 'mensajes.html', {'mensaje': mensaje,'nombre': nombre, 'mensajes_enviados':mensajes_enviados, 'mensajes_recibidos': mensajes_recibidos})

