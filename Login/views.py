from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
# Create your views here.


def login_request(request):
    
    if request.method == 'POST':

        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid:
            usu= request.POST['username']
            clave= request.POST['password']

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render (request, "index.html", {'form':form, 'mensaje': f"Bienvenido {usuario}"})
            else:
                return render (request, "login.html", {'form':form, 'mensaje': f"Usuario o clave incorrectos"})
        else:
            return render (request, "login.html", {'form':form, 'mensaje': f"Formulario invalido"})
    else:
        form = AuthenticationForm()
        return render (request, "login.html", {'form':form})