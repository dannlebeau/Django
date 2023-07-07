from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import VehiculoForm, RegistroUsuarioForm
from .models import VehiculoModel
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
#Creación de vista inicio(Drilling Final, Parte 2)
def inicio(request):
           
    context ={}           
            
    return render(request, 'index.html', context)
#Creación del método input_models(Drilling Final, Parte 2)
def input_models(request):
    context = {}
    form = VehiculoForm(request.POST or None, request.FILES or None)
    #Sí el formulario está correcto se redirecciona a index
    if form.is_valid():
        form.save()
        messages.success(request, "El vehículo se agregado exitosamente")
        return HttpResponseRedirect('/')
    
    context['form'] = form
    return render(request,'add.html', context)

#Creación de vista navbar(Drilling Final, Parte 3)
def navbar(request):
    context = {}
    return render(request, 'navbar.html', context)

def registro_usuario(request):
    #Primer if para verificar que el usuario no esté en la BD
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        #Segundo if para verificar que la información esté correcta
        if form.is_valid():
            user = form.save()
            #Se obtiene el content_type del módelo
            content_type = ContentType.objects.get_for_model(VehiculoModel)
            #Se obtiene el permiso a asignar
            visualizar_catalogo = Permission.objects.get(
                codename='visualizar_catalogo',
                content_type=content_type
            )
            #Se agrega permiso al usuario
            user.user_permissions.add(visualizar_catalogo)
            #Sí está correcto el usuario, se iniciará sesión automáticamente
            user = form.save()
            login(request, user)
            messages.success(request, "¡Bienvenido a Vehiculos.com, te has registrado exitosamente")
            return HttpResponseRedirect('/navbar')
        #De lo contrario generará un mensaje error
        messages.error(request, "¡Oops ocurrió un error! Algunos datos son incorrectos")
    form = RegistroUsuarioForm()
    context = {"register_form" : form } 
    return render(request, "registro.html", context)

#Creación método login_vehiculo, inicio sesión de un usuario (Drilling Final, parte 4)
def login_vehiculo(request):
    #Validación de Datos
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            #Sí las credenciales son correctas, se inicia sesión:
            if user is not None:
                login(request, user)
                messages.info(request, f"Te has logueado como: {username}.")
                return HttpResponseRedirect('/navbar')
            #Sí los campos son invalidos:
            else:
                messages.error(request, "El usuario o la constraseña no son correctas")
        
    form = AuthenticationForm()
    context = {"login_form": form}
    return render(request, 'login.html', context)

#Creación método logout_vehiculo, cierre de Sesión del usuario (Drilling Final, parte 4)
def logout_vehiculo(request):
    logout(request)
    messages.info(request, "Se ha cerrado la sesión satisfactoriamente")
    return HttpResponseRedirect('/login')

#Creación del método listar_vehiculo(Drilling Final, Parte 4)
def listar_vehiculo(request):
    lista = VehiculoModel.objects.all()
    
    context = {
        'listas': lista                     
            }
    return render(request, 'lista.html', context)