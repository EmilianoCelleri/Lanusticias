from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import Editar_perfil
# Create your views here.

@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        formulario = Editar_perfil(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()
            return render (request, "index.html", {'usuario':usuario, 'mensaje': f"PERFIL EDITADO EXITOSAMENTE"})

    else:
        formulario=Editar_perfil(instance=usuario)
    return render (request, "editar_perfil.html", {'formulario':formulario, 'usuario': usuario.username})