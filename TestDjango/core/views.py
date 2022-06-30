from distutils.log import error
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django. views. decorators. csrf import csrf_exempt
from carro.carro import Carro
from core.forms import ProductoForm, CustomUserCreationForm, DonacionForm
from .models import *
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.authtoken.models import Token
import requests
from django.http import Http404
from django.contrib import messages
from django.http import JsonResponse
import json
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def index(request):
    
    carro = Carro(request)
    
    productos = Producto.objects.all()
    
    data = {
        'productos' : productos
    }
    
    return render(request, 'core/index.html', data)

def Carrito(request):
    return render(request, 'core/Carrito.html')

def donacion(request):
    return render(request, 'core/donacion.html')

def Gato(request):
    return render(request, 'core/Gato.html')

def Perro(request):
    return render(request, 'core/Perro.html')

def tarjeta(request):
    return render(request, 'core/tarjeta.html')

def todos(request):
    return render(request, 'core/todos.html')


def modificar(request):
    return render(request, 'core/modificar.html')


def widget(request):
    return render(request, 'carro/widget.html')

def checkout(request):
    return render(request, 'carro/checkout.html')

def custom_login(request):
    return render(request, 'registration/customlogin.html')



@csrf_exempt
@permission_required('app.view_producto')
def listar(request):
    productosListado = Producto.objects.all()
    page = request.GET.get('page', 1)
    
    try:
        paginator = Paginator(productosListado, 5)
        productosListado = paginator.page(page)

    except:
        raise Http404

    datos= {
            'entity': productosListado,
            'paginator' : paginator
        }  
    
    return render(request, 'core/listar.html', datos)


@csrf_exempt
@permission_required('app.add_producto')
def agregar(request):
    datos= {
        'form' : ProductoForm()
    }  
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado correctamente!")
        else:
            datos["form"] = formulario
    
    return render(request, 'core/agregar.html', datos)


@csrf_exempt
@permission_required('app.delete_producto')
def eliminarProducto(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="/listar" )
    #return redirect(to="listar")

@csrf_exempt
@permission_required('app.change_producto')
def modificarProducto(request, idProducto):
    
    producto = get_object_or_404(Producto, idProducto=idProducto)
    
    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado correctamente")
            return redirect(to="listar")
        data["form"] = formulario
        
    return render(request,  'core/modificar.html', data)


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="/custom_login")
        data["form"] = formulario        
    return render(request, 'registration/customlogin.html', data)


@csrf_exempt
@login_required
def crear_suscripcion(request):
    token = Token.objects.get(user=request.user)
    headers = {'Authorization': f'Token {token}'}

    # Consultar suscripciones
    url_lista = "http://127.0.0.1:8000/api/lista_donacion"
    suscripciones = requests.get(url_lista, headers=headers).json()
    
    datos= {
        'form' : DonacionForm()
    }  
    
    # Buscar si usuario esta suscrito y obtener suscripcion
    for i in suscripciones:
        if i['suscriptor'] == request.user.id:
            id = i['id']
            url_detalle = f'http://127.0.0.1:8000/api/detalle_donacion/{id}'
            datos['suscripcion'] = requests.get(url_detalle, headers=headers).json()
    
    if request.method == 'POST':
        formulario = DonacionForm(data=request.POST)
        
        if formulario.is_valid():
            copia_dict = request.POST.copy()
            copia_dict['suscriptor'] = request.user.id
            requests.post(url_lista, headers=headers, json=copia_dict)
            messages.success(request, "¡Gracias por tu donacion! Has sido beneficiado con un 5% de descuento en tu próxima compra.")
            formulario.save()
            return redirect(to="index")
        else:
            datos["form"] = formulario
    
    return render(request, 'core/suscripcion.html', datos)

@login_required
def lista_suscripciones(request):

    url = "http://127.0.0.1:8000/api/lista_donacion"
    token = Token.objects.get(user=request.user)
    headers = {'Authorization': f'Token {token}'}

    suscripciones = requests.get(url, headers=headers).json()

    data = {
        'suscripciones' : suscripciones,
    }

    return render(request, 'suscripciones/listar.html', data)


@login_required
def cancelar_suscripcion(request, id): 

    url = f'http://127.0.0.1:8000/api/detalle_donacion/{id}'
    token = Token.objects.get(user=request.user)
    headers = {'Authorization': f'Token {token}'}

    requests.delete(url, headers=headers)
    messages.info(request, "Al apretar esta acción no podras volver atrás.", extra_tags='Suscripcion Cancelada')
    
    return redirect(to="index")

# MODIFICAR SUSCRIPCION (REST)
@login_required
def modificar_suscripcion(request, id): 

    url = f'http://127.0.0.1:8000/api/detalle_donacion/{id}'
    token = Token.objects.get(user=request.user)
    headers = {'Authorization': f'Token {token}'}

    suscripcion = requests.get(url, headers=headers).json()
    
    data = {
        'form' : DonacionForm(data=suscripcion)
    }

    if request.method == 'POST':
        formulario = DonacionForm(data=request.POST)
        if formulario.is_valid():
            requests.put(url, headers=headers, json=request.POST)
            messages.success(request, "Se ha modificado correctamente.", extra_tags='Modificada')
            return redirect(to="lista_suscripciones")
        else:
            data["form"] = formulario
    
    return render(request, 'suscripciones/modificar.html', data)

def custom_login(request):
    hola = "hola"
    data = {
        'form' : AuthenticationForm,
        'saludo' : hola
    }
    if request.method == 'POST':
        formulario = AuthenticationForm(data=request.POST)

        if formulario.is_valid():
            url = "http://127.0.0.1:8000/api/login_user"
            requests.post(url, json=request.POST)
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password"])
            login(request, user)
            return redirect(to="index")
        else:
            data['form'] = formulario
    return render(request, 'registration/customlogin.html', data)