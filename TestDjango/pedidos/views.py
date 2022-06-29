from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from pedidos.models import Pedido, LineaPedido
from carro.carro import Carro
from django.contrib import messages
from core.models import Producto

# Create your views here.
login_required(login_url="/accounts/login")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():     #por cada clave, valor que haya en los items del carro, estamos recorriendo elementos del carro
        lineas_pedido.append(LineaPedido( # aqui rescatamos cada uno de los items
            producto_id = Producto.objects.get(idProducto = key),
            cantidad = value["cantidad"],
            user = request.user,
            pedido_id = pedido
            
            
        ))
        
    LineaPedido.objects.bulk_create(lineas_pedido) # este metodo es un INSERT INTO 
    
    messages.success(request, "El pedido se ha creado correctamente!")
    
    return redirect("/")
    
    