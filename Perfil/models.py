from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User



class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True, blank=True)


class Perfil(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    descripcion=models.CharField(max_length=200, null=True, blank=True)
    web=models.URLField(null=True, blank=True)

# Create your models here.

