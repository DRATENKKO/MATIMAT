from django import forms
from django.forms import ModelForm, ValidationError
from .models import Producto, Cliente, Donacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50)
    precio = forms.IntegerField(min_value=1, max_value=1500000)
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre=nombre).exists()
        
        if existe:
            raise ValidationError("Este nombre ya existe")
        return nombre
    
    class Meta:
        model = Producto
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm): 
    class Meta: 
        model = User
        fields = ['username',"first_name","last_name","email","password1", "password2"]
        
             

class ClienteForm(ModelForm):
    class Meta:
       model = Cliente
       fields = '__all__'
              
class DonacionForm(ModelForm):
    
    nombrecompleto = forms.CharField(min_length=3, max_length=50)
    correo = forms.EmailField(max_length=254)
    telefono = forms.IntegerField(max_value=999999999)
    valor = forms.IntegerField(min_value=1000, max_value=1500000)
    
    
    class Meta:
       model = Donacion
       fields = '__all__'
        
        
    
