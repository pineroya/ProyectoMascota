from django.db import models

# Create your models here.

class Perros(models.Model):
    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    duenio=models.CharField(max_length=50)
    raza=models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

class Gatos(models.Model):
    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    duenio=models.CharField(max_length=50)
    raza=models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

class Conejos(models.Model):
    nombre=models.CharField(max_length=40)
    edad=models.IntegerField()
    duenio=models.CharField(max_length=50)
    raza=models.CharField(max_length=40)

    def __str__(self):
        return self.nombre