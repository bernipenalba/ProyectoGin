from django.shortcuts import render, get_object_or_404, redirect
from Productos.models import Producto, Categoria
from Productos.forms import ProductoForm, CategoriaForm

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/listar_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/agregar_producto.html', {'form': form})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('listar_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request, 'productos/confirmar_eliminar_producto.html', {'producto': producto})

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'productos/listar_categorias.html', {'categorias': categorias})

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'productos/agregar_categoria.html', {'form': form})

