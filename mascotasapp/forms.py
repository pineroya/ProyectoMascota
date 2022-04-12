from django import forms

class Formularioform(forms.Form):
    nombre = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    duenio = forms.CharField(max_length=50)
    color = forms.CharField(max_length=40)