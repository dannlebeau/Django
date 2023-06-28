from django import forms

from .models import BoardsModel

class InputForm(forms.Form):
    nombre = forms.CharField(max_length=200)
    apellido = forms.CharField(max_length=200)
    prioridad = forms.IntegerField(min_value=1, max_value=3)
    contrasena = forms.CharField(widget=forms.PasswordInput())

class BoardsForm(forms.ModelForm):
    class Meta:
        model = BoardsModel
        fields = "__all__"
        #exclude = ["descripcion"]