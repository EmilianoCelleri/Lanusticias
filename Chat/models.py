from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Mensaje(models.Model):
    cuerpo=models.CharField(max_length=300)
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Emisor')
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Receptor')
    enviado = models.DateTimeField(auto_now_add=True)
    leido=models.BooleanField(default=False)

    def __str__(self):
        return f"De: {self.emisor} Para: {self.receptor}"

    class Meta:
        ordering = ['-enviado']

