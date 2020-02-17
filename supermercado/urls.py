from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('supermercado/sucursales', views.SucursalesView)

urlpatterns = [
    path('', include(router.urls))
]