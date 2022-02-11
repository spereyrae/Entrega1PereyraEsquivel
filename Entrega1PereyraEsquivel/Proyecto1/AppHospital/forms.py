from django import forms

class medicoformulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    matricula = forms.IntegerField()

class pacienteformulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    dni = forms.IntegerField()
    email = forms.EmailField()

class especialidadformulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    codigo = forms.IntegerField()