from django.shortcuts import render
from rest_framework import viewsets
from .models import Sucursales
from .serializers import SucursalesSerializer

class SucursalesView(viewsets.ModelViewSet):
    queryset = Sucursales.objects.all()
    serializer_class = SucursalesSerializer    
