# importar la librería estándar de Django Forms
from django import forms
from .models import VehiculoModel
# Agregando para el registro de usuarios 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

#Creación ModelForm (Drilling Final, parte 1 y 2)
class VehiculoForm(forms.ModelForm): 
    #Específica el nombre del modelo a usar
    class Meta: 
        model = VehiculoModel 
        fields = "__all__" #para que se puedan usar todos

# Clase para el registro de usuarios 
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True) 
    # Especifica el nombre del modelo a usar
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
    
    def save(self, commit=True):
        user = super(RegistroUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user