from django.db import models
"""
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
"""
from django.db import models


class Cliente (models.Model):
    nombre = models.CharField (max_length=20)   
    dni = models.IntegerField()    
    email = models.EmailField ()                  
    celular = models.IntegerField ()