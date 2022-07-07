from django.contrib import admin

from .models import Pedido, LineaPedido, EnvioDireccion

# Register your models here.

admin.site.register(Pedido)
admin.site.register(LineaPedido)
admin.site.register(EnvioDireccion)
