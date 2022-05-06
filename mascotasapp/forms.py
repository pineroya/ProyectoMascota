from django import forms
from PIL import Image
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.files.uploadedfile import SimpleUploadedFile
from blog.models import Post
from home.models import User

class Formularioform(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    duenio = forms.CharField(max_length=50)
    color = forms.CharField(max_length=40)

class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    first_name = forms.CharField()
    last_name = forms.CharField()

    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name']
    #     help_texts = {k:"" for k in fields}

class FormularioBlog(forms.ModelForm):
    
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=50)
    contenido = forms.CharField(max_length=500)
    imagen = forms.ImageField()

    class Meta:
        model = Post
        fields = ['imagen']

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label = "Modificar E-mail")
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir contraseña", widget=forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = ['email', 'password', 'password2']
    #     help_texts = {k:"" for k in fields}