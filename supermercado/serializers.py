from rest_framework import serializers
from .models import Sucursales

class SucursalesSerializer(serializers.ModelSerializer): # solo modelserializar y corchetes
    class Meta: 
        model = Sucursales
        fields = ['id','url', 'sucursal', 'direccion', 'mapa', 'telefono']