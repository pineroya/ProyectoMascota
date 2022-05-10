from django import forms
from PIL import Image
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from mascotasapp.models import mascotaApp
from home.models import Avatar, Profile
from blog.models import Post

class FormularioMascota(forms.Form):

    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    duenio = forms.CharField(max_length=50)
    color = forms.CharField(max_length=40)
    tipo = forms.CharField(max_length=20)


class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class FormularioBlog(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'autor',]
    
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=50)
    contenido = forms.CharField(max_length=500)
    imagen = forms.ImageField()
    autor = forms.TextInput()


class UserEditForm(UserChangeForm):

    email = forms.EmailField(label = "Modificar E-mail", widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
        help_texts = {k:"" for k in fields}


# class ProfilePageForm(forms.ModelForm):
#     class Meta:
#         model=Profile
#         fields=('bio','website_url')
#         widgets={'bio':forms.Textarea(attrs={'class':'form-control'}), 'website_url':forms.TextInput(attrs={'class':'form-control'}),
            
#             #'profile_pic':forms.
#             }

class AvatarFormulario(forms.Form):
    imagen = forms.ImageField(required=True)


class FormularioContacto(forms.Form):
    asunto = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField()