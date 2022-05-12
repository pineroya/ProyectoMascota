from django.shortcuts import render
from .models import mascotaApp
from django.template import loader
from django.http import HttpResponse
from mascotasapp.forms import Formulario_mascota
from django.contrib.auth.decorators import login_required
from home.models import Avatar

# Create your views here.

@login_required
def nuestras_mascotas(request):

    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request, "mascotas/nuestras_mascotas.html", {"url":avatares[0].imagen.url})

@login_required
def listado_animales(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    
    mascotalis = mascotaApp.objects.all()

    return render(request, "mascotas/listado_mascotas.html", {"mascotalis":mascotalis, "url":avatares[0].imagen.url})

@login_required
def busqueda_mascota(request):

    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request, "mascotas/busqueda_mascota.html", {"url":avatares[0].imagen.url})

@login_required
def resultado_busqueda(request):

    avatares = Avatar.objects.filter(user=request.user.id)

    if request.GET["bmascota"]:

        busquedamas = request.GET["bmascota"]
        mascota = mascotaApp.objects.filter(nombre__icontains=busquedamas)
        return render(request, "mascotas/resultado_busqueda.html", {"mascota": mascota, "query": busquedamas, "url":avatares[0].imagen.url})

    else:

        mensaje="Dato ingresado incorrecto"

    return HttpResponse(mensaje)

@login_required
def formulario(request):

    avatares = Avatar.objects.filter(user=request.user.id)

    if request.method=="POST":

        miformulario = Formulario_mascota(request.POST)

        if miformulario.is_valid():

            informacion = miformulario.cleaned_data
            mascotaf = mascotaApp(nombre=informacion['nombre'],
            edad=informacion['edad'], duenio=informacion['duenio'], color=informacion['color'], tipo=informacion['tipo'])
            mascotaf.save()

            return render(request, "mascotas/nuestras_mascotas.html")
    
    else:
        miformulario = Formulario_mascota()

    return render(request, "mascotas/formulario.html", {"miformulario": miformulario, "url":avatares[0].imagen.url})
