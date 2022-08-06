from django.urls import path
from .views import *


urlpatterns = [
   

   path('paneladmin', paneladmin, name='paneladmin'),
   path('panel/nuevo', BlogCreacion.as_view(), name='blog_crear'),   
   path('panel/list/', BlogList.as_view(), name='blog_list'),
   path('panel/editar/<pk>', BlogUpdate.as_view(), name='blog_editar'),
   path('panel/detalle/<pk>', BlogDetalle.as_view(), name='blog_detalle'),
   path('panel/borrar/<pk>', BlogDelete.as_view(), name='blog_borrar'),



]