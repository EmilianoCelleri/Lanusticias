from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Blog(models.Model):

    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50, null=True)
    contenido = models.TextField(max_length=300)
    imagen = models.ImageField(upload_to='Blog')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-creado']

    def __str__(self):
        return self.titulo
