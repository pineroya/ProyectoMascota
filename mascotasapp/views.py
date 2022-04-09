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

def listado_perros(request):

    perros=Perros.objects.all()
    return render(request, "listado_mascotas.html", {"perro":perros})

def listado_gatos(request):

    gatos=Gatos.objects.all()
    print(gatos)
    return render(request, "listado_mascotas.html", {"gato":gatos})

def listado_conejos(request):
    conejos=Conejos.objects.all()
    print(conejos)
    return render(request, "listado_mascotas.html", {"conejo":conejos})

