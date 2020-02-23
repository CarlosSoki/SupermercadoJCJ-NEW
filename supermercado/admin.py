from django.contrib import admin
from .models import Sucursales
from .models import Categoria
from .models import Producto
from .models import Precio
from .models import Inventario
from .models import UserDetails
from .models import Carrito


#########################################################################
class SucursalesAdmin(admin.ModelAdmin):

    list_display = ('id','sucursal', 'direccion','telefono', 'mapa', 'on_off')
    list_filter = ('on_off',)
    search_fields = ('sucursal',)
    ordering = ('id',)

admin.site.register(Sucursales, SucursalesAdmin)
#########################################################################
class CategoriaAdmin(admin.ModelAdmin):

    list_display = ('nombre_categoria','id',)
    #list_filter = ()
    search_fields = ('nombre_categoria',)
    ordering = ('nombre_categoria',)

admin.site.register(Categoria, CategoriaAdmin)
#########################################################################
class ProductoAdmin(admin.ModelAdmin):

    list_display = ('id','nombre','descripcion', 'imagen', 'id_categoria_id','id_categoria')
    list_filter = ('id_categoria',)
    search_fields = ('nombre',)
    ordering = ('id',)

admin.site.register(Producto, ProductoAdmin)
#########################################################################
class PrecioAdmin(admin.ModelAdmin):

    list_display = ('id','id_producto','id_producto_id', 'fecha_hora', 'precio')
    list_filter = ('id_producto_id',)
    #search_fields = ('id_producto',)
    ordering = ('fecha_hora',)

admin.site.register(Precio, PrecioAdmin)
#########################################################################
class InventarioAdmin(admin.ModelAdmin):

    list_display = ('id','id_sucursal','id_producto','id_precio','unidades_ex')
    list_filter = ('id_sucursal','id_producto')
    #search_fields = ('id_sucursal',)
    ordering = ('id',)

admin.site.register(Inventario, InventarioAdmin)
#########################################################################
class UserDetailsAdmin(admin.ModelAdmin):

    list_display = ('id','id_usuario_id','id_usuario','fecha_nacimiento','sexo','cedula','telefono')
    list_filter = ('sexo',)
    #search_fields = ('id_usuario',)
    ordering = ('id',)

admin.site.register(UserDetails, UserDetailsAdmin)
#########################################################################
class CarritoAdmin(admin.ModelAdmin):

    list_display = ('id','id_usuario_id','id_usuario','id_inventario','id_inventario_id','on_off')
    list_filter = ('id_usuario','id_inventario', 'on_off')
    #search_fields = ('id_sucursal',)
    ordering = ('id',)

admin.site.register(Carrito, CarritoAdmin)

