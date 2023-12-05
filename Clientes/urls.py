from django.urls import path
from Clientes.views import listar_clientes, detalle_cliente, agregar_cliente, editar_cliente, eliminar_cliente

urlpatterns = [
    path('listar/', listar_clientes, name='listar_clientes'),
    path('<int:cliente_id>/', detalle_cliente, name='detalle_cliente'),
    path('agregar/', agregar_cliente, name='agregar_cliente'),
    path('editar/<int:cliente_id>/', editar_cliente, name='editar_cliente'),
    path('eliminar/<int:cliente_id>/', eliminar_cliente, name='eliminar_cliente'),
]