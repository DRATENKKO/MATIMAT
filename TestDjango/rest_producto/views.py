from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes # sin este no puedo crear la api
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Producto
from .serializers import ProductoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_productos(request):
    #discriminar si es GET O POST  
    if request.method=='GET':
        productos = Producto.objects.all() #<=> SELECT * FROM Producto
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_producto(request, id):
    try: # busco un producto por id
        producto = Producto.objects.get(idProducto=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET': # obtengo los datos de UN PRODUCTO por su id 
        serializer=ProductoSerializer(producto)
        return Response(serializer.data)

    if request.method=='PUT': 
        data = JSONParser().parse(request)
        serializer = ProductoSerializer(producto, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method=='DELETE': # elimino un producto por su id
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


