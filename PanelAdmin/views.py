from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from Blog.models import Blog
 
# Create your views here.


def paneladmin(request):
    return render (request, 'paneladmin.html')


class BlogCreacion(CreateView, LoginRequiredMixin):
    model = Blog
    success_url = reverse_lazy('blogs')
    template_name="blog_form.html"
    fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'imagen']

class BlogList(ListView, LoginRequiredMixin):
    model = Blog
    template_name="blog_list.html"


class BlogUpdate(UpdateView, LoginRequiredMixin):
    model = Blog
    success_url= reverse_lazy('blog_list')
    template_name="blog_form.html"
    fields = ['titulo', 'subtitulo', 'contenido', 'autor', 'imagen']

class BlogDetalle(DetailView, LoginRequiredMixin):
    model = Blog
    template_name="blog_detalle.html"

class BlogDelete(DeleteView, LoginRequiredMixin):
    model = Blog
    success_url = reverse_lazy('blog_list')
    template_name="blog_confirm_delete.html"






def eliminar_blog(request, id): 
    blog = Blog.objects.get(id=id)
    blog.delete()

    return render (request, "index.html", {"mensaje": f"La entrada ha sido eliminada"} )