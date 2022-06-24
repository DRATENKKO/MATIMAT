from asyncore import read
from numpy import source
from rest_framework import serializers
from core.models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    nombre_categoria = serializers.CharField(read_only=True, source="categoria.nombreCategoria")
    class Meta:
        model = Producto
        fields = '__all__'
        

#class DonacionSerializer(serializers.ModelSerializer):
    
#    def validate_nombre(self, value):
#        existe = Producto.objects.filter(nombre=value).exists()
#        if (existe):
#            raise serializers.ValidationError("Este nombre ya existe")
#        return value

#    class Meta:
#        model = Donacion
#        fields = '__all__'
        