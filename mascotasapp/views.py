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

