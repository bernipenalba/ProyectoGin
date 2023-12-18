from django import forms
from Ventas.models import Venta
"""
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'producto', 'cantidad']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Puedes personalizar el formulario aquí si es necesario
        # Por ejemplo, puedes agregar clases CSS, atributos de estilo, etc.
"""

class VentasForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ('cliente','productos','total',)
        exclude = ['fecha_venta']