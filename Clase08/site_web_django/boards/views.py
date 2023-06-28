from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
import datetime
from .forms import InputForm, BoardsForm, RegistroUsuarioForm
from tokenize import PseudoExtras
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

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

def registro_view(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrado Satisfactoriamente.")
        return HttpResponseRedirect("/menu")
    
    messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
    form = RegistroUsuarioForm()
    context = { "register_form" : form }
    return render(request, "registro.html", context)

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Iniciaste sesión como: {username}.")
                return HttpResponseRedirect("/menu")
            else:
                messages.error(request,"Invalido username o password.")
        else:
            messages.error(request,"Invalido username o password.")
    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente.")
    return HttpResponseRedirect("/menu")
