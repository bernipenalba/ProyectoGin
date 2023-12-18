from django import forms
from Clientes.models import Cliente
"""
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'email', 'telefono', 'direccion']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Puedes personalizar el formulario aquí si es necesario
        # Por ejemplo, puedes agregar clases CSS, atributos de estilo, etc.
"""

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nombre','dni','email','celular',)