from django.urls import path
#Importación de las vistas
from .views import inicio, input_models, navbar, registro_usuario, listar_vehiculo, login_vehiculo, logout_vehiculo

urlpatterns = [
   #Se agrega la url "index",(Drilling Final, parte 2)
   path('', inicio, name = 'index'),
   #Se agrega la url "vehiculo/add",(Drilling Final, parte 2)
   path('vehiculo/add', input_models, name = 'vehiculo/add'),
   #Se agrega la url "navbar",(Drilling Final, parte 3)
   path('navbar/', navbar, name = 'navbar'),
   #Se agrega la url "registro",(Drilling Final, parte 4)
   path('registro/', registro_usuario, name = 'registro'),
   #Se agrega la url "login",(Drilling Final, parte 4)
   path('login/', login_vehiculo, name = 'login'),
   #Se indica vista "logout"(Drilling Final, parte 4)
   path('logout/', logout_vehiculo, name='logout'),
   #Se agrega la url "list",(Drilling Final, parte 4)
   path('vehiculo/list', listar_vehiculo, name = 'vehiculo/list'),
   
  
]