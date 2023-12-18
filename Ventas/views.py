from django.shortcuts import render
from Ventas.forms import VentasForm

def Venta_form (request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = VentasForm()
    return render(request, 'ventas/ventas_form.html', {'form': form})

"""
from django.shortcuts import render, get_object_or_404, redirect
from Ventas.models import Venta
from Ventas.forms import VentaForm

def listar_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'ventas/listar_ventas.html', {'ventas': ventas})

def detalle_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    return render(request, 'ventas/detalle_venta.html', {'venta': venta})

def agregar_editar_venta(request, venta_id=None):
    venta = None
    if venta_id:
        venta = get_object_or_404(Venta, pk=venta_id)

    if request.method == 'POST':
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            form.save()
            return redirect('listar_ventas')
    else:
        form = VentaForm(instance=venta)

    return render(request, 'ventas/agregar_editar_venta.html', {'form': form, 'venta': venta})

def eliminar_venta(request, venta_id):
    venta = get_object_or_404(Venta, pk=venta_id)
    if request.method == 'POST':
        venta.delete()
        return redirect('listar_ventas')

    return render(request, 'ventas/confirmar_eliminar_venta.html', {'venta': venta})

"""