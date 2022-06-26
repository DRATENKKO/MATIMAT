from tabnanny import verbose
from venv import create
from django.db import models
from core.models import Producto
from django.db.models import F, Sum, IntegerField
# Create your models here.


class Pedido(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id
    
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
    
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido_id = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self): 
        return f'{self.cantidad} unidades de {self.producto_id.nombre}'

        
    class Meta:
        db_table='lineapedidos'
        verbose_name = 'Linea Pedido'
        verbose_name_plural = 'Lineas Pedidos'
        ordering = ['id']  