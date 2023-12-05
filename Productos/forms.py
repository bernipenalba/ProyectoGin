from django import forms
from Productos.models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Puedes personalizar el formulario aquí si es necesario
        # Por ejemplo, puedes agregar clases CSS, atributos de estilo, etc.

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Puedes personalizar el formulario aquí si es necesario
        # Por ejemplo, puedes agregar clases CSS, atributos de estilo, etc.
