from rest_framework import serializers
from .models import Sucursales
from .models import Categoria
from .models import Producto
from .models import Precio
from .models import Inventario
from .models import UserDetails
from .models import Carrito

class SucursalesSerializer(serializers.ModelSerializer): # solo modelserializar y corchetes
    class Meta: 
        model = Sucursales
        fields = ['id','url', 'sucursal', 'direccion', 'mapa', 'telefono', 'on_off']

class CategoriaSerializer(serializers.ModelSerializer): # solo modelserializar y corchetes
    class Meta: 
        model = Categoria
        fields = ['id','url', 'nombre_categoria']

class ProductoSerializer(serializers.ModelSerializer): # solo modelserializar y corchetes
    class Meta: 
        model = Producto
        fields = ['id','url', 'nombre', 'descripcion', 'imagen', 'id_categoria']

class PrecioSerializer(serializers.ModelSerializer): # solo modelserializar y corchetes
    class Meta: 
        model = Precio
        fields = ['id','url', 'id_producto', 'fecha_hora', 'precio']

class InventarioSerializer(serializers.ModelSerializer): # solo modelserializar y corchetes
    class Meta: 
        model = Inventario
        fields = ['id','url', 'id_sucursal', 'id_producto', 'id_precio', 'unidades_ex']

class UserDetailsSerializer(serializers.ModelSerializer): # solo modelserializar y corchetes
    class Meta: 
        model = UserDetails
        fields = ['id','url', 'id_usuario', 'fecha_nacimiento', 'sexo', 'cedula', 'telefono']

class CarritoSerializer(serializers.ModelSerializer): # solo modelserializar y corchetes
    class Meta: 
        model = Carrito
        fields = ['id','url', 'id_usuario', 'id_inventario', 'cantidad', 'on_off']
        