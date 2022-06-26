from asyncore import read
from numpy import source
from rest_framework import serializers
from core.models import Producto, Donacion

class ProductoSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.CharField(read_only=True, source="categoria.nombreCategoria")
    class Meta:
        model = Producto
        fields = '__all__'
        

class DonacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Donacion
        fields = '__all__'
        