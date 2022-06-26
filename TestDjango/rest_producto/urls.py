from django.urls import path, include
from rest_producto.views import lista_productos, detalle_producto, lista_donacion, detalle_donacion
from rest_producto.viewslogin import login_user
from rest_framework import routers


urlpatterns = [
    path('lista_productos', lista_productos, name='lista_productos'),
    path('detalle_producto/<id>', detalle_producto, name='detalle_producto'),
    path('login_user', login_user, name='login_user'),
    path('lista_donacion', lista_donacion, name='lista_donacion'),
    path('detalle_donacion/<id>', detalle_donacion, name='detalle_donacion'),
]
