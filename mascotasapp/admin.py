from django.contrib import admin
from .models import *

# Register your models here.

class MascotaAdmin(admin.ModelAdmin):
    list_display=("nombre", "edad", "duenio", "color", "tipo")

admin.site.register(mascotaApp, MascotaAdmin)