from django import forms
from django.forms import ModelForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
class ProductoForm(ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    pass


