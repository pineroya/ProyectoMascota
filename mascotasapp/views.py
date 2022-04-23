from django.shortcuts import render
from .models import Perros, Gatos, Conejos
from django.template import loader
from django.http import HttpResponse
from mascotasapp.forms import Formularioform

# Create your views here.

def listado_animales(request):

    perros=Perros.objects.all()
    gatos=Gatos.objects.all()
    conejos=Conejos.objects.all()
    return render(request, "mascotas/listado_mascotas.html", {"perro":perros, "gato": gatos, "conejo": conejos})

def busqueda_mascota(request):

    return render(request, "mascotas/busqueda_mascota.html")

def buscar(request):

    if request.GET["bmascota"]:

        #mensaje="Mascota buscada: %r" %request.GET["bmascota"]
        busquedapet = request.GET["bmascota"]
        petperro = Perros.objects.filter(nombre__icontains=busquedapet)
        petgato = Gatos.objects.filter(nombre__icontains=busquedapet)
        petconejo = Conejos.objects.filter(nombre__icontains=busquedapet)
        return render(request, "mascotas/resultado_busqueda.html", {"petperro": petperro, "query": busquedapet, "petgato": petgato, "query": busquedapet, "petconejo": petconejo, "query": busquedapet})

    else:

        mensaje="Dato ingresado incorrecto"

    return HttpResponse(mensaje)

def formulario(request):

    if request.method=="POST":

        miformulario = Formularioform(request.POST)
        print(miformulario)

        if miformulario.is_valid():

            informacion = miformulario.cleaned_data
            perrof = Perros(nombre=informacion['nombre'], edad=informacion['edad'], duenio=informacion['duenio'], color=informacion['color'])
            perrof.save()
            return render(request, "mascotas/listado_mascotas.html")
    
    else:
        miformulario = Formularioform()

    return render(request, "mascotas/formulario.html", {"miformulario": miformulario})