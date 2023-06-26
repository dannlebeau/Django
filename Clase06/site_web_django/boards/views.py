from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

import datetime

# Create your views here.

class Persona(object):
    def __init__(self, nombre, apellido, login):
        self.nombre = nombre
        self.apellido = apellido
        self.login = login

def index(request):
    return HttpResponse("Mensaje, Hola Mundo")

class IndexPageView(TemplateView):
    template_name = "index.html"

def obtenerFecha(request, name="Pep"):
    fechaActual = datetime.datetime.now()

    
    context = {
        "fecha": fechaActual,
        "name": name,
    }

    return render(request, "fecha.html", context)


def menuView(request):
    context = {}
    return render(request, "menu.html", context)

def mostrar(request):
    persona = Persona("Juan", "Perez", True)
    items = ["Manzana", "Pera", "Durazno", "Platano", "Piña"]
    
    context = {
        "nombre": persona.nombre,
        "apellido": persona.apellido,
        "login": persona.login,
        "items": items
    }
    return render(request, "example.html", context)
