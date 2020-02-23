from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('sucursales', views.SucursalesView)
router.register('categoria', views.CategoriaView)
router.register('producto', views.ProductoView)
router.register('precio', views.PrecioView)
router.register('inventario', views.InventarioView)
router.register('userdetails', views.UserDetailsView)
router.register('carrito', views.CarritoView)


urlpatterns = [
    path('', include(router.urls))
]