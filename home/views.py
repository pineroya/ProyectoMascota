from django.shortcuts import HttpResponse, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from mascotasapp.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from .models import User

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

def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "home/home.html")

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
    
    return render(request, 'home/registration/editarperfil.html', {'miFormulario': miFormulario, 'usuario': usuario})

def password_change_done(request):
    return render(request, "home/registration/password_reset_done.html")#2