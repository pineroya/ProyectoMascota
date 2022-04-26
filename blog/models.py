from typing import ForwardRef
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    titulo=models.CharField(max_length=50)
    subtitulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=500)
    imagen=models.ImageField(upload_to='blog/img', null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.titulo
