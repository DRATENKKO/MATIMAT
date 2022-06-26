from django.shortcuts import render

from .carro import Carro

from core.models import Producto

from django.shortcuts import redirect
# Create your views here.

def agregar_producto (request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(idProducto = producto_id)
    carro.agregar(producto=producto)
    return redirect ("index")

def agregar_productoo (request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(idProducto = producto_id)
    carro.agregar(producto=producto)
    return redirect ("checkout")

def restar_productoo (request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(idProducto = producto_id)
    carro.restar_producto(producto=producto)
    return redirect ("checkout")

def eliminar_producto (request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(idProducto = producto_id)
    carro.eliminar(producto=producto)
    return redirect ("core/index.html")

def restar_producto (request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(idProducto = producto_id)
    carro.restar_producto(producto=producto)
    return redirect ("index")

def limpiar_carro (request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect ("index")
