from django.contrib import admin
from .models import *
# Register your models here.

class PerrosAdmin(admin.ModelAdmin):
    list_display=("nombre", "edad", "duenio", "color")

admin.site.register(Perros, PerrosAdmin)

class GatosAdmin(admin.ModelAdmin):
    list_display=("nombre", "edad", "duenio", "color")

admin.site.register(Gatos, GatosAdmin)

class ConejosAdmin(admin.ModelAdmin):
    list_display=("nombre", "edad", "duenio", "color")

admin.site.register(Conejos, ConejosAdmin)
