from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django. views. decorators. csrf import csrf_exempt

from core.forms import ProductoForm, CustomUserCreationForm, DonacionForm
from .models import Producto, Donacion
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request):
    
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
        
        if formulario.is_valid:
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
            return redirect(to="index")
        data["form"] = formulario        
    return render(request, 'registration/registro.html', data)


def donacion(request):
    donacionListado = Donacion.objects.all()
    
    datos= {
            'donacion': donacionListado
        }  
    return render(request, 'core/donacion.html', datos)


def agregardonacion(request):
    datos= {
        'form' : DonacionForm()
    }  
    if request.method == 'POST':
        formulario = DonacionForm(request.POST, files=request.FILES)
        
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "¡Gracias por tu donacion! Has sido beneficiado con un 5% de descuento en tu próxima compra.")
        else:
            datos["form"] = formulario
    
    return render(request, 'core/agregardonacion.html', datos)

    



#class Persona:
    #def __init__(self,nombre,edad):
        #self.nombre=nombre
       # self.edad=edad
        #super().__init__()

#def test(request):
    #lista=["lasaña","Charquican","Porotos verdes"]
    #hijo=Persona("JUANITO","10")
    #contexto={"nombre":"anita la huerfanita","comidas": lista, "hijo":hijo}
    #return render(request, 'core/test.html',contexto)
