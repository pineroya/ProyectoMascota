import imp
from django.shortcuts import HttpResponse, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login, logout, authenticate
from mascotasapp.forms import UserRegisterForm, UserEditForm, FormularioContacto, AvatarFormulario
from django.contrib.auth.decorators import login_required
from .models import Avatar
from django.contrib.auth.models import User
from mascotasapp import views
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views import generic

@login_required
def home(request):

    return render(request, "home/home.html")

def aboutus(request):
    return render(request, "home/aboutus.html")

def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, "home/home.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, "home/home.html", {"mensaje": "Error, datos incorrectos"})
        
        else:
            return render(request, "home/home.html", {"mensaje":"Error, formulario erroneo"})
    
    form = AuthenticationForm()
    return render(request, "home/registration/login.html", {'form': form})

@login_required
def miPerfil(request):

    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request, 'home/mi_perfil.html', {"url":avatares[0].imagen.url})

def register(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "home/home.html", {"mensaje":"Usuario Creado con éxito"})
    
    else:
        form = UserRegisterForm()

    return render(request, "home/registration/registro.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()

            return render(request, "home/mi_perfil.html")

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, 'home/registration/editarperfil.html', {'miFormulario': miFormulario, 'usuario': usuario})

@login_required
def agregarAvatar(request):
    if request.method == "POST":

        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            u = User.objects.get(username=request.user)

            avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen'])

            avatar.save()

            return render (request, "home/home.html")

    else:

        miFormulario=AvatarFormulario()

    return render (request, "home/agregar_avatar.html", {'miFormulario': miFormulario})



def contacto(request):
    if request.method == "POST":

        miFormulario = FormularioContacto(request.POST)

        if miFormulario.is_valid():

            infForm=miFormulario.cleaned_data

            send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email', ''), ['paulaortizmenne@gmail.com'],)

            return render(request, "home/contacto_ok.html")

    else:

        miFormulario = FormularioContacto()

    return render (request, "home/formulario_contacto.html", {"miFormulario" : miFormulario})

def contacto_enviado(request):
    return render(request, "home/contacto_ok.html")

def password_change_done(request):
    return render(request, "home/registration/password_reset_done.html")