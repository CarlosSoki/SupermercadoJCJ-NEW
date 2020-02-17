from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('supermercado/sucursales', views.SucursalesView)
router.register('supermercado/categoria', views.CategoriaView)
router.register('supermercado/producto', views.ProductoView)
router.register('supermercado/precio', views.PrecioView)
router.register('supermercado/inventario', views.InventarioView)
router.register('supermercado/userdetails', views.UserDetailsView)
router.register('supermercado/carrito', views.CarritoView)


urlpatterns = [
    path('', include(router.urls))
]