from django.db import models
from django.conf import settings

#################################################################################################################
class Sucursales(models.Model):  #lo segundo crear el modelo de la tabla
    sucursal = models.CharField(blank=False, unique=True, max_length=50, verbose_name='Nombre Sucursal:', help_text='Inglese la sucursal')
    direccion = models.CharField(blank=False, unique=True, max_length=150, verbose_name='Direción Sucursal:', help_text='Inglese dirección sucursal')
    mapa = models.CharField(blank=False, unique=True, max_length=100, verbose_name='Link Google:', help_text='Ingrese el Mapa de la sucursal')
    telefono = models.CharField(unique=True, blank=False, max_length=20,  verbose_name='Telefono:',  help_text='Inglese telefono')
    on_off = models.BooleanField(default=True, verbose_name='Sucursal Activa:',  help_text='Inglese el estado de la sucursal')

    def __str__(self):
        return self.sucursal

    class Meta:
        ordering = ['sucursal']
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'
#################################################################################################################
class Categoria(models.Model):  #lo segundo crear el modelo de la tabla
    nombre_categoria = models.CharField(blank=False, unique=True,  max_length=50, verbose_name='Categoria:', help_text='Inglese el nombre de la Categoria')
    
    def __str__(self):
        return self.nombre_categoria

    class Meta:
        ordering = ['nombre_categoria']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
#################################################################################################################
class Producto(models.Model):  #lo segundo crear el modelo de la tabla
    nombre = models.CharField(blank=False, unique=True, max_length=50, verbose_name='Nombre:', help_text='Inglese el Nombre del producto')
    descripcion = models.TextField(blank=True, max_length=100, verbose_name='Descripcion:', help_text='Ingrese la Descripción del prodcuto')
    imagen = models.FileField(upload_to='image_produc', blank=False, verbose_name='Imagen Producto:', help_text='Ingrese la imagen del prodcuto')
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria Producto:', help_text='Ingrese la categoria del producto')
    
    def __str__(self):
        return self.nombre #, self.precio, self.descripcion

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
#################################################################################################################
class Precio(models.Model): 
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto:', help_text='Ingrese el nombre del producto')
    fecha_hora = models.DateTimeField(auto_now=True) #auto_now_add=true hora cuando se crea el objeto
    precio = models.IntegerField(null=False, blank=False, verbose_name='Precio:', help_text='Inglese el precio del producto en $')

    class Meta:
        verbose_name = 'Precio'
        verbose_name_plural = 'Precios'
#################################################################################################################
class Inventario(models.Model):  #lo segundo crear el modelo de la tabla
    id_sucursal = models.ForeignKey(Sucursales, on_delete=models.CASCADE, verbose_name='Sucursal:', help_text='Ingrese el nombre de la sucursal')
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto:', help_text='Ingrese el nombre del producto')
    id_precio = models.ForeignKey(Precio, on_delete=models.CASCADE, verbose_name='Precio:', help_text='Cree un nuevo precio para el producto')
    unidades_ex = models.IntegerField(null=False, blank=False, verbose_name='Unidades Existentes:', help_text='Ingrese las unidades del producto')

    class Meta:
        unique_together = (('id_sucursal','id_producto'),)

        verbose_name = 'Inventario'
        verbose_name_plural = 'Inventarios'
#################################################################################################################
class UserDetails(models.Model):
    MASCULINO = 'M'
    FEMENINO = 'F'
    INDEFINIDO ='I'
    SEXO_CHOICES = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
        (INDEFINIDO, 'Indefinido'),
    ]

    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuario:', help_text='Ingrese el usuario')
    fecha_nacimiento = models.DateField(verbose_name='Fecha Nacimiento:', help_text='Ingrese la fecha de nacimiento')
    sexo = models.CharField(max_length=1, choices = SEXO_CHOICES, default = INDEFINIDO, verbose_name='Sexo:', help_text='Ingrese su sexo')
    cedula = models.CharField(blank=True, unique=True, max_length=20, verbose_name='Cedula:', help_text='Ingrese su numero de cedula')
    telefono = models.CharField(blank=False, unique=True, max_length=20,  verbose_name='Telefono:',  help_text='Inglese telefono')

    class Meta:
        verbose_name = 'Detalles Usuario'
        verbose_name_plural = 'Detalles Usuarios'
#################################################################################################################
class Carrito(models.Model):  #lo segundo crear el modelo de la tabla

    id_usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Usuario:', help_text='Ingrese el usuario')
    id_inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, verbose_name='Inventario:', help_text='Ingrese inventario que decea agregar al carrito')
    cantidad = models.IntegerField(null=False, blank=False, default=1, verbose_name='Cantidad:', help_text='Inglese la cantidad de productos')
    on_off = models.BooleanField(default=True, verbose_name='Producto Activo:',  help_text='Inglese el estado del producto en el carrito')    

    class Meta:
        unique_together = (('id_usuario','id_inventario'),)

        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'