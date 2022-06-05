from contextlib import nullcontext
from typing import TextIO
from django.db import models

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
    precio = models.CharField(max_length=9)
    stock = models.IntegerField()
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    especie = models.ForeignKey(CategoriaEspecie, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.idProducto, self.nombre)
    
class Donacion(models.Model):
    idDonante = models.IntegerField(primary_key=True)
    nombreD = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.IntegerField()
    donacion = models.IntegerField()

    def _str_(self):
        texto = "{0} ({1})"
        return texto.format(self.nombreD,self.donacion)



