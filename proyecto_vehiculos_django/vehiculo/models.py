from django.db import models

# Create your models here.
#Creación de Modelo Vehiculo (Drilling Final, parte 1)
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
    
    #Se crea Class Meta para creación de permisos(Drilling Final, parte 4)
    class Meta:
              
        permissions = (
            ("visualizar_catalogo", "Puede visualizar catálogo vehículo"),
           
        )
    
    def __str__(self):
        return self.marca