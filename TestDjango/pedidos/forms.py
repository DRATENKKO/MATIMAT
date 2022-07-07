from django.forms import ModelForm
from .models import EnvioDireccion


class EnvioDireccionForm(ModelForm):
    class Meta:
       model = EnvioDireccion
       fields = ["direccion","ciudad","region","codigo_postal"]


        