from django.urls import path
from Productos.views import listar_productos, detalle_producto,agregar_producto, editar_producto, eliminar_producto
from Productos.views import listar_categorias, agregar_categoria

urlpatterns = [
    path('listar/', listar_productos, name='listar_productos'),
    path('<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('agregar/', agregar_producto, name='agregar_producto'),
    path('editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('eliminar/<int:producto_id>/', eliminar_producto, name='eliminar_producto'),
    path('listar_categorias/', listar_categorias, name='listar_categorias'),
    path('agregar_categoria/', agregar_categoria, name='agregar_categoria'),
]
