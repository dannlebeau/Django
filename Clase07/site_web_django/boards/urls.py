from django.urls import path
#from.import views
from .views import IndexPageView, obtenerFecha, menuView, mostrar, datosform_view, formmanual_view, boardsform_view


urlpatterns =[
    path("", IndexPageView.as_view(), name ="index"),
    path("fecha/<name>", obtenerFecha, name="fecha_name"),
    path("fecha/", obtenerFecha, name="fecha"),
    path("menu/", menuView, name="menu"),
    path("mostrar/", mostrar, name ="mostrar"),
    path("datosform/", datosform_view, name ="datosform"),
    path("formmanual/", formmanual_view, name ="formmanual"),
    path("boardsform/", boardsform_view, name ="boardsform"),

]

