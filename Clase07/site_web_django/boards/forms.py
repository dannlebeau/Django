from django import forms

from .models import BoardsModel
class InputForm(forms.Form):
    nombre = forms.Charfield(max_length=200)
    apellido = forms.Charfield(max_length=200)
    prioridad = forms.Integerfield(min_value=1, max_value=3)
    contrasena = forms.Charfield(widget=forms.PasswordInput())

    class BoardsForm(forms.ModelForm):
        class Meta:
            model = BoardsModel
            fields = "__all__"
            #exclude = ["descripcion"]