from django.urls import path
from Ventas.views import listar_ventas, detalle_venta, agregar_editar_venta, eliminar_venta

urlpatterns = [
    path('listar/', listar_ventas, name='listar_ventas'),
    path('<int:venta_id>/', detalle_venta, name='detalle_venta'),
    path('agregar/', agregar_editar_venta, name='agregar_venta'),
    path('editar/<int:venta_id>/', agregar_editar_venta, name='editar_venta'),
    path('eliminar/<int:venta_id>/', eliminar_venta, name='eliminar_venta'),
]
