from tabnanny import verbose
from venv import create
from django.db import models
from core.models import Producto
from django.db.models import F, Sum, IntegerField
from django.contrib.auth.models import User
# Create your models here.


class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total = Sum(F("precio")*F("cantidad"), output_field = IntegerField())
        )["total"]
    
    class Meta:
        db_table='pedidos'
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['id']    
        
class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self): 
        return f'usuario: {self.user} | | pedido: {self.pedido_id} | | compró {self.cantidad} unidades de {self.producto_id.nombre}'

        
    class Meta:
        db_table='lineapedidos'
        verbose_name = 'Linea Pedido'
        verbose_name_plural = 'Lineas Pedidos'
        ordering = ['id']  
        
        
class EnvioDireccion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=True, db_constraint=False)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, default=True, db_constraint=False)
    direccion = models.CharField(max_length=200, null=True)
    ciudad = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    codigo_postal = models.CharField(max_length=200, null=True)
    fecha_sumar = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'usuario: {self.user} | |  direccion: {self.direccion}'

