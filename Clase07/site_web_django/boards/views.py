from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.views.generic import TemplateView

import datetime
from .forms import InputForm, BoardsForm

# Create your views here.

def datosform_view(request):
    context = { "form": InputForm()}
    return render(request, "datosform.html", context)


def formmanual_view(request):
    context = {"form": InputForm()}
    return render(request, "formmanual.html", context)

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


def boardsform_view(request):
    context = {}

    form = BoardsForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    
    context["form"] = form
    return render(request,"datosform.html", context)


