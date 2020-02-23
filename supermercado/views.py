from django.shortcuts import render
from rest_framework import viewsets
from .models import Sucursales
from .models import Categoria
from .models import Producto
from .models import Precio
from .models import Inventario
from .models import UserDetails
from .models import Carrito
from .serializers import SucursalesSerializer
from .serializers import CategoriaSerializer
from .serializers import ProductoSerializer
from .serializers import PrecioSerializer 
from .serializers import InventarioSerializer
from .serializers import UserDetailsSerializer
from .serializers import CarritoSerializer

class SucursalesView(viewsets.ModelViewSet):
    queryset = Sucursales.objects.all()
    serializer_class = SucursalesSerializer    

class CategoriaView(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer    

class ProductoView(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class PrecioView(viewsets.ModelViewSet):
    queryset = Precio.objects.all()
    serializer_class = PrecioSerializer

class InventarioView(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class UserDetailsView(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetailsSerializer

class CarritoView(viewsets.ModelViewSet):
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

#def producto_with_price():