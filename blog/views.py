from django.shortcuts import render
from blog.models import *
from django.template import loader
from django.http import HttpResponse
from ProyectoMascotas import settings
from django.conf import settings
from django.contrib.auth.decorators import login_required
from mascotasapp.forms import FormularioBlog

# Create your views here.

@login_required
def blog(request):

    posts=Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def formularioblog(request):
        if request.method=="POST":

            formulariob = FormularioBlog(request.POST, request.FILES)

            if formulariob.is_valid():

                informacionblog = formulariob.cleaned_data
                formblog = Post(titulo=informacionblog['titulo'], subtitulo=informacionblog['subtitulo'],
                contenido=informacionblog['contenido'], imagen=informacionblog['imagen'],autor=informacionblog['autor'])
                formblog.save()
                return render(request, "blog/formblog.html")
        
        else:
            formulariob = FormularioBlog()

        return render(request, "blog/formblog.html", {"formulariob": formulariob})

def deletepost(request, titulo_blog):

    dblog = Post.objects.get(titulo = titulo_blog)
    dblog.delete()

    dblogs = Post.objects.all()

    contexto = {"dblogs": dblogs}

    return render(request, "blog/blog.html", contexto)

def editarblog(request, titulo_blog):

    eblog = Post.objects.get(titulo = titulo_blog)

    if request.method == 'POST':

        formulariob = FormularioBlog(request.POST, request.FILES)

        print(formulariob)

        if formulariob.is_valid():

            informacionblog = formulariob.cleaned_data

            eblog.titulo = informacionblog['titulo']
            eblog.subtitulo = informacionblog['subtitulo']
            eblog.contenido = informacionblog['contenido']
            eblog.imagen = informacionblog['imagen']
            eblog.save()

            return render(request, "blog/blog.html")
    else:
        formulariob = FormularioBlog(initial={'titulo': eblog.titulo, 'subtitulo': eblog.subtitulo, 'contenido': eblog.contenido, 'imagen': eblog.imagen})
    
    return render(request, 'blog/editarblog.html', {'formulariob': formulariob, 'titulo_blog': titulo_blog})
    