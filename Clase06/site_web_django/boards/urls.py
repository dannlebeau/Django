from django.urls import path
#from.import views
from .views import IndexPageView, obtenerFecha, menuView, mostrar


urlpatterns =[
    path("", IndexPageView.as_view(), name ="index"),
    path("fecha/<name>", obtenerFecha, name="fecha_name"),
    path("fecha/", obtenerFecha, name="fecha"),
    path("menu/", menuView, name="menu"),
    path("mostrar/", mostrar, name ="mostrar"),

]

