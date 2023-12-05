from django.db import models
from Clientes.models import Cliente
from Productos.models import Producto

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_venta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.producto} - {self.cantidad} unidades"

