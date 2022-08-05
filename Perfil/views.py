from operator import contains
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PerfilEditForm, UserEditForm, AvatarForm
from .models import Avatar, Perfil
# Create your views here.

@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        formulario = UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.set_password(formulario.cleaned_data.get('password1'))
                      
            usuario.save()
            return render (request, "index.html", {'usuario':usuario, 'mensaje': f"Perfil editado exitosamente"})

    else:
        formulario=UserEditForm(instance=usuario)
    return render (request, "editar_perfil.html", {'formulario':formulario, 'usuario': usuario.username})


@login_required
def mostrar_perfil(request):
    
    usuario=request.user
    
    imagen=Avatar.objects.filter(user_id=request.user.id)[0].imagen.url
    informacion=Perfil.objects.get(user_id=request.user)
    if(informacion):
        user=Perfil.objects.get(user_id=request.user)
        web=user.web
        descripcion=user.descripcion
    


    return render (request, "mostrar_perfil.html", {'imagen': imagen, 'usuario':usuario.username, 'nombre': usuario.first_name, 'apellido':usuario.last_name, 'web': web, 'descripcion': descripcion})

@login_required
def agregar_avatar(request):

    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            
            avatar_viejo=Avatar.objects.filter(user_id=request.user.id)
            if(avatar_viejo):
                avatar_viejo.delete()
            avatar=Avatar(user=request.user,imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render (request, "index.html", {'usuario':request.user, 'mensaje': f"Avatar agregado exitosamente"})
    else:
        formulario = AvatarForm()
        return render (request, "agregar_avatar.html", {'formulario':formulario, 'usuario': request.user})



'''@login_required
def editar_informacion(request):
    usuario = request.user

    if request.method == 'POST':
        formulario = PerfilEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion=formulario.cleaned_data
            usuario.web = informacion['web']
            usuario.descripcion = informacion['descripcion']                                 
            usuario.save()
            return render (request, "index.html", {'usuario':usuario, 'mensaje': f"PERFIL EDITADO EXITOSAMENTE"})

    else:
        formulario=PerfilEditForm(instance=usuario)
    return render (request, "editar_informacion.html", {'formulario':formulario, 'usuario': usuario.username})'''
    


@login_required
def editar_informacion(request):

    if request.method == 'POST':
        formulario=PerfilEditForm(request.POST)
        if formulario.is_valid():
            
            info_vieja=Perfil.objects.filter(user_id=request.user.id)
            if(info_vieja):
                info_vieja.delete()
            informacion=Perfil(user=request.user,web=formulario.cleaned_data['web'],descripcion=formulario.cleaned_data['descripcion'])
            informacion.save()
            return render (request, "index.html", {'usuario':request.user, 'mensaje': f"La informacion se edito exitosamente"})
    else:
        formulario = PerfilEditForm()
        return render (request, "editar_informacion.html", {'formulario':formulario, 'usuario': request.user})
