from django.urls import path
from .views import index, donacion, Carrito, Gato, Perro, tarjeta, todos, listar, modificar,\
agregar, eliminarProducto, modificarProducto, registro,widget,crear_suscripcion,\
lista_suscripciones,cancelar_suscripcion, modificar_suscripcion,checkout, custom_login

urlpatterns = [
    path('', index, name='index'),
    path('donacion/', donacion, name='donacion'),
    path('Carrito/', Carrito, name='Carrito'),
    path('Gato/', Gato, name='Gato'),
    path('Perro/', Perro, name='Perro'),
    path('tarjeta/', tarjeta, name='tarjeta'),
    path('todos/', todos, name='todos'),
    path('listar/', listar, name='listar'), 
    path('modificar/', modificar, name='modificar'), 
    path('agregar/', agregar, name='agregar'),
    path('eliminarProducto/<idProducto>', eliminarProducto, name='eliminarProducto'),
    path('modificarProducto/<idProducto>', modificarProducto, name='modificarProducto'),
    path('registro/', registro, name='registro'),
    path('widget/', widget, name="widget"),
    path('checkout/', checkout, name="checkout"),
    #path('actualizar_item/', actualizarItem, name="actualizar_item"), 
    path('suscribirse/', crear_suscripcion, name="suscribirse"),
    path('suscripciones/', lista_suscripciones, name="lista_suscripciones"), 
    path('cancelarsuscripcion/<id>/', cancelar_suscripcion, name="cancelar"), 
    path('modificarsuscripcion/<id>/', modificar_suscripcion, name="modificar_suscripcion"), 
    path('custom_login', custom_login, name="custom_login"),
]