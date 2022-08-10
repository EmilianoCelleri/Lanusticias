from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.


class Blog(models.Model):

    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=50, null=True)
    contenido = RichTextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Autor')
    imagen = models.ImageField(upload_to='Blog')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.titulo
