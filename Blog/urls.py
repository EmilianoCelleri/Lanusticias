from django.urls import path
from WebApp import views
from Blog import views


urlpatterns = [
   


    path('blog/<id>', views.blog, name='blog'),
    path('blogs', views.blogs, name='blogs'),
    path('buscar', views.buscar, name='buscar'),
    path('busqueda_blog', views.busqueda_blog, name='busqueda_blog'),


]