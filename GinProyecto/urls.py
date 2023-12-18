from django.contrib import admin
from django.urls import path, include
from Clientes import views as clientes_views
from Productos import views as productos_views
from Ventas import views as ventas_views
"""urlpatterns = [
    path('admin/', admin.site.urls),
    path('Clientes/', include('Clientes.urls')),
    path('Productos/', include('Productos.urls')),
    path('Ventas/', include('Ventas.urls'))
]
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Clientes/', clientes_views.Cliente_form, name='Cliente_form'),
    path('Productos/', productos_views.Producto_form, name='Producto_form'),
    path('Ventas/', ventas_views.Venta_form, name='Venta_form'),
]