from django.db import models
from django.contrib.auth.models import User, Group, Permission #linea para permisos

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def assign_visualizar_catalogo_permission(sender, instance, created, **kwargs):
    if created:
        # Verificar si el permiso ya existe
        visualizar_perm = Permission.objects.filter(codename='visualizar_catalogo').first()
        
        # Crear el permiso solo si no existe
        if not visualizar_perm:
            visualizar_perm = Permission.objects.create(
                codename='visualizar_catalogo',
                name='Puede visualizar Catálogo de Vehículos',
                content_type_id=9  # Reemplazar el ID de ContentType correspondiente a la app o modelo del Catálogo de Vehículos
            )
            
        # Asignar el permiso al usuario
        instance.user_permissions.add(visualizar_perm)


# Create your models here.
#Creación de Modelo Vehiculo 
#Definicón de lista de opciones de marca
vehiculo_marca = [
    ('Fiat', 'Fiat'),
    ('Chevrolet', 'Chevrolet'),
    ('Ford', 'Ford'),
    ('Toyota', 'Toyota')
]
#Definicón de lista de opciones de categoria
vehiculo_categoria = [
    ('Particular', 'Particular'),
    ('Transporte', 'Transporte'),
    ('Carga', 'Carga')
    ]

class VehiculoModel(models.Model):
    marca = models.CharField(max_length=20, null=False, blank=False,
                                choices=vehiculo_marca, default= 'Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, null=False, blank=False,
                                choices=vehiculo_categoria, default= 'Particular')
    precio = models.IntegerField()
    creado= models.DateTimeField(auto_now_add=True)
    modificado= models.DateTimeField(auto_now=True)
    
    #Se crea Class Meta para creación de permisos
    class Meta:
              
        permissions = (
            ("visualizar_catalogo", "Puede visualizar catálogo vehículo"),
           
        )
    
    def __str__(self):
        return self.marca