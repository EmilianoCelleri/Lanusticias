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

    return render (request, 'chat.html', {'mensajes':mensajes})



'''@login_required
def mandar_mensaje(request):
    
    if (request.method=="POST"):
        form=MandarMensajeForm(request.POST)
        
        if form.is_valid():
            info=form.cleaned_data
            
            cuerpo=info["cuerpo"]
            receptor=info["receptor"]
            mensaje=Mensaje(cuerpo=cuerpo, receptor=receptor, emisor=request.user)
            mensaje.save()
            return render (request, "chat.html")    
    else:
        form=MandarMensajeForm()
    return render (request, "mandar_mensaje.html", {"formulario": form})'''


class MandarMensaje(CreateView, LoginRequiredMixin):
    model = Mensaje
    template_name="mensaje_form.html"
    success_url = reverse_lazy('chat')
    fields = ['cuerpo','receptor']

    def form_valid(self, form):
        """Forzar el usuario a Request.user"""
        self.mensaje = form.save(commit=False)
        self.mensaje.emisor_id = self.request.user.id
        self.mensaje.save()

        return super(MandarMensaje, self).form_valid(form)
    