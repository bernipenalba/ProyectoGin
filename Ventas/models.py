from django.db import models
#from Clientes.models import Cliente
#from Productos.models import Producto
"""
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.producto} - {self.cantidad} unidades"

"""
from django.db import models

class Venta(models.Model):
    cliente = models.CharField(max_length=100)
    productos = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venta {self.id} - {self.cliente}"
