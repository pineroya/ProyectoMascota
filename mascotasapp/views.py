from django.shortcuts import render
from .models import mascotaApp
from django.template import loader
from django.http import HttpResponse
from mascotasapp.forms import FormularioMascota
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def nuestras_mascotas(request):
    return render(request, "mascotas/nuestras_mascotas.html")

@login_required
def listado_animales(request):

    mascotalis = mascotaApp.objects.all()

    return render(request, "mascotas/listado_mascotas.html", {"mascotalis":mascotalis})

@login_required
def busqueda_mascota(request):

    return render(request, "mascotas/busqueda_mascota.html")

@login_required
def resultado_busqueda(request):

    if request.GET["bmascota"]:

        busquedapet = request.GET["bmascota"]
        mascota = mascotaApp.objects.filter(nombre__icontains=busquedapet)
        return render(request, "mascotas/resultado_busqueda.html", {"mascota": mascota, "query": busquedapet})

    else:

        mensaje="Dato ingresado incorrecto"

    return HttpResponse(mensaje)

@login_required
def formulario(request):

    if request.method=="POST":

        miformulario = FormularioMascota(request.POST)
        print(miformulario)

        if miformulario.is_valid():

            informacion = miformulario.cleaned_data
            mascotaf = mascotaApp(nombre=informacion['nombre'],
            edad=informacion['edad'], duenio=informacion['duenio'], color=informacion['color'], tipo=informacion['tipo'])
            mascotaf.save()

            return render(request, "mascotas/nuestras_mascotas.html")
    
    else:
        miformulario = FormularioMascota()

    return render(request, "mascotas/formulario.html", {"miformulario": miformulario})
