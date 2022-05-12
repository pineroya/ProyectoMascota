from django.shortcuts import render
from blog.models import *
from django.template import loader
from django.http import HttpResponse
from ProyectoMascotas import settings
from django.conf import settings
from django.contrib.auth.decorators import login_required
from mascotasapp.forms import Formulario_blog
from home.models import Avatar

# Create your views here.

@login_required
def blog(request):

    posts=Post.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request, "blog/blog.html", {"posts": posts, "url":avatares[0].imagen.url})

def formulario_blog(request):
        if request.method=="POST":

            formulariob = Formulario_blog(request.POST, request.FILES)

            if formulariob.is_valid():

                informacionblog = formulariob.cleaned_data
                formblog = Post(titulo=informacionblog['titulo'], subtitulo=informacionblog['subtitulo'], contenido=informacionblog['contenido'], imagen=informacionblog['imagen'], autor=informacionblog['autor'])
                formblog.save()
                return render(request, "blog/formblog.html")
        
        else:
            formulariob = Formulario_blog()

        return render(request, "blog/formblog.html", {"formulariob": formulariob})

def borrar_blog(request, titulo_blog):

    bblog = Post.objects.get(titulo = titulo_blog)
    bblog.delete()

    bblogs = Post.objects.all()

    contexto = {"bblogs": bblogs}

    return render(request, "blog/blog.html", contexto)

def editar_blog(request, titulo_blog):

    eblog = Post.objects.get(titulo = titulo_blog)

    if request.method == 'POST':

        formulariob = Formulario_blog(request.POST, request.FILES)

        if formulariob.is_valid():

            informacionblog = formulariob.cleaned_data

            eblog.titulo = informacionblog['titulo']
            eblog.subtitulo = informacionblog['subtitulo']
            eblog.contenido = informacionblog['contenido']
            eblog.imagen = informacionblog['imagen']
            eblog.save()

            return render(request, "blog/blog.html")
    else:
        formulariob = Formulario_blog(initial={'titulo': eblog.titulo, 'subtitulo': eblog.subtitulo, 'contenido': eblog.contenido, 'imagen': eblog.imagen})
    
    return render(request, 'blog/editarblog.html', {'formulariob': formulariob, 'titulo_blog': titulo_blog})
