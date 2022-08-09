from django.shortcuts import get_object_or_404, render
from Blog.models import Blog
from django.views.generic import TemplateView

# Create your views here.

def blogs(request):

    blogs=Blog.objects.all()
    
    return render (request, 'blogs.html', {'blogs':blogs})


def blog(request, id):

    blog=get_object_or_404(Blog, id=id)

    return render (request, 'blog.html', {'blog':blog})

class Error404(TemplateView):
    template_name = '404.html'

def busqueda_blog(request):
    return render (request, "busqueda_blog.html")

def buscar(request):
    if request.GET["titulo"]:
        tit=request.GET["titulo"]
        blogs=Blog.objects.filter(titulo__icontains=tit)
        return render (request, "resultados_busqueda.html", {"blogs":blogs})
    else:
        return render(request, "busqueda_blog.html", {"error": "No se ingreso ningun nombre" })
