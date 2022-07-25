from django.urls import path
from WebApp import views
from Blog import views


urlpatterns = [
   


    path('blog/', views.blog, name='blog'),


]