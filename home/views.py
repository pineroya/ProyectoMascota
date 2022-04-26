from django.shortcuts import HttpResponse, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from mascotasapp.forms import UserRegisterForm

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
    return render(request, "home/login.html", {'form': form})


def register(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "home/home.html", {"mensaje":"Usuario Creado con éxito"})
    
    else:
        form = UserRegisterForm()

    return render(request, "home/registro.html", {"form": form})