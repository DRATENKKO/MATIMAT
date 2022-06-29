from contextlib import nullcontext
from email.policy import default
from signal import default_int_handler
from typing import TextIO
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

class CategoriaProducto(models.Model):
    idCategoria = models.IntegerField(primary_key=True)
    nombreCategoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreCategoria
    
class CategoriaEspecie(models.Model):
    idEspecie = models.IntegerField(primary_key=True)
    nombreEspecie = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreEspecie
    
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    especie = models.ForeignKey(CategoriaEspecie, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.idProducto, self.nombre)
    
    
class Cliente(models.Model):
    idCliente = models.IntegerField(primary_key=True)
    nombreCliente = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.idCliente, self.nombreCliente)
    
    
    
class Donacion(models.Model):   
    suscriptor = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    nombredonante = models.CharField(max_length=50)
    telefono = models.IntegerField()
    valor = models.IntegerField()
    fecha = models.DateTimeField(auto_now= True)
    estado = models.BooleanField(default = True, null = True)
    

    def _str_(self):
        return self.nombredonante
    
    

