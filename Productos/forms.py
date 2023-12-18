from django import forms
from Productos.models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre', 'precio','stock',)
        exclude = ['fecha_creacion']