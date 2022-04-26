from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class Formularioform(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    duenio = forms.CharField(max_length=50)
    color = forms.CharField(max_length=40)

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    # class Meta:
    #     model = User
    #     fields = ['username', 'mail', 'password', 'password2']
    #     help_text = {k:"" for k in fields}