from django.shortcuts import render
from Blog.models import Blog

# Create your views here.


def inicio(request):
    #blogs = Blog.objects.all()
    blogs = Blog.objects.all()[0:3]
    return render (request, "index.html", {'blogs': blogs})

def about(request):
    return render (request, "about.html")
