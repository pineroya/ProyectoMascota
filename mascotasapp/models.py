from tabnanny import verbose
from django.db import models

# Create your models here.

class mascotaApp(models.Model):
    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    duenio=models.CharField(max_length=50)
    color=models.CharField(max_length=40)
    tipo=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
