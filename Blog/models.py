from django.db import models

# Create your models here.


class Blog(models.Model):

    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='Blog')
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.titulo
