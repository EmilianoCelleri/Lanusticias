from django.shortcuts import render
from Blog.models import Blog

# Create your views here.

def blogs(request):

    blogs=Blog.objects.all()
    
    return render (request, 'blogs.html', {'blogs':blogs})


def blog(request, id):

    blog=Blog.objects.get(id=id)

    return render (request, 'blog.html', {'blog':blog})