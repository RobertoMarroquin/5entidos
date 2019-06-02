#Librerias de Django
from django.db import models

#Librerias de Python
import datetime

class Proveedor(models.Model):

    Nombre = models.CharField(blank=True, max_length=100)
    Telefono = models.IntegerField(blank=True, null=True)
    Direccion = models.TextField(blank=True)
    Correo = models.EmailField()

    def __str__(self):
        return self.Nombre


class Producto(models.Model):

    Nombre = models.CharField(blank=True, max_length=100)
    Tipo = models.CharField(blank=True, max_length=100)
    Cantidad = models.IntegerField(blank=True, null=True)
    PrecioCompra = models.DecimalField(max_digits=5, decimal_places=2)
    PrecioVenta = models.DecimalField(max_digits=5, decimal_places=2)
    Descripcion = models.TextField(blank=True)
    Foto = models.ImageField(upload_to="static/media/",null=True,blank=True)

    def __str__(self):
        return f"{self.Nombre}"


class RegistroCompra(models.Model):
    """(RegistroCompra description)"""

    FechaCompra = models.DateTimeField(blank=True, default=datetime.datetime.now)
    Producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    Proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    Cantidad = models.IntegerField(blank=True, null=True)
    Valor = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{Producto.Nombre}-{Proveedor.Nombre}"
