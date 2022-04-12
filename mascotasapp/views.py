from django.shortcuts import render
from .models import Perros, Gatos, Conejos
from django.template import loader
from django.http import HttpResponse

# Create your views here.


"""def listado_perros(request):
    template = loader.get_template('listado_mascotas.html')

    perros=Perros.objects.all()
    print(perros)
    context = {
        'perros': perros,
    }
    return HttpResponse(template.render(context, request))"""

def listado_animales(request):

    perros=Perros.objects.all()
    gatos=Gatos.objects.all()
    conejos=Conejos.objects.all()
    return render(request, "listado_mascotas.html", {"perro":perros, "gato": gatos, "conejo": conejos})

def busqueda_mascota(request):

    return render(request, "busqueda_mascota.html")

def buscar(request):

    if request.GET["bmascota"]:

        #mensaje="Mascota buscada: %r" %request.GET["bmascota"]
        busquedapet=request.GET["bmascota"]
        petperro=Perros.objects.filter(nombre__icontains=busquedapet)
        return render(request, "resultado_busqueda.html", {"petperro": petperro, "query": busquedapet})

    else:

        mensaje="Dato ingresado incorrecto"

    return HttpResponse(mensaje)