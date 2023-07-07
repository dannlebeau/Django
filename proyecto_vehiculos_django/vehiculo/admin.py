from django.contrib import admin

# Register your models here.

from .models import VehiculoModel
#Creación class BookAdmin para mostrar en sitio de Admin(Drilling Final, parte 4)
class VehiculoAdmin(admin.ModelAdmin):
    readonly_fields = ('creado', 'modificado')
    list_display = ('marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio')
    list_filter = ('precio', 'modificado')
    
    #Creación de campo dinámico Condicion de Precio (Drilling Final, parte 4)
    def condicion_de_precio(self):
        if self.precio > 30000:
            return "Alto" 
        elif  self.precio > 10000 and self.precio <= 30000:
            return "Media"
        elif self.precio <= 10000: 
            return "Baja"
#Registro de App Vehiculo a sitio Django(Drilling Final, Parte 1)
admin.site.register(VehiculoModel, VehiculoAdmin)
