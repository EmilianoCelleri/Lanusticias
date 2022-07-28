from django.urls import path
from WebApp import views
from Blog import views


urlpatterns = [
   


    path('blog/<id>', views.blog, name='blog'),
    path('blogs', views.blogs, name='blogs'),


]