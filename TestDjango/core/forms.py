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
            # en self.changed_data esta todo lo que ingrso el usuario en el formulario.
        nombre = self.cleaned_data["nombre"]
        existe = False
                
        # Validar si el nombre existe en la base de datos
        #if Producto.id ==0:
        if not self.instance.pk:
          existe = Producto.objects.filter(nombre=nombre).exists()
         
        # si existe mostar un error al usuario
        if existe:
          raise ValidationError("Este nombre ya existe...")
        return nombre
       
    class Meta:
        model = Producto
        fields =  ["nombre","precio","stock","categoria","especie", "imagen"]

class CustomUserCreationForm(UserCreationForm): 
    class Meta: 
        model = User
        fields = ['username',"first_name","last_name","email","password1", "password2"]
        
             
class ClienteForm(ModelForm):
    class Meta:
       model = Cliente
       fields = '__all__'
       
class DonacionForm(forms.ModelForm):
    
    nombredonante = forms.CharField(min_length=3, max_length=50, label="Nombre completo")
    telefono = forms.IntegerField(max_value=999999999, label="Telefono")
    valor = forms.IntegerField(min_value=1000, max_value=1500000, label="Monto")
       
    class Meta:
       model = Donacion
       fields = ["nombredonante", "telefono","valor"]


              
        
        
  