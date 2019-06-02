#Modulos de Django
from django.db import models
#Modulos de App
from Usuarios.models import Usuario
from Inventario.models import Producto
#Modulos python
import datetime


class Venta(models.Model):
    """(Venta description)"""
    Fecha = models.DateTimeField(blank=True, default=datetime.datetime.now)
    Total = models.DecimalField(max_digits=5, decimal_places=2)
    IVATotal = models.DecimalField(max_digits=5, decimal_places=2)
    Cliente = models.ForeignKey('Usuarios.Usuario',on_delete=models.CASCADE,related_name="Cliente")
    Empleado = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="Empleado")

    def __str__(self):
        return f"{self.Cliente} {self.Fecha}"

class LineaVenta(models.Model):
    """(RegistoVenta description)"""
    Subtotal = models.DecimalField(max_digits=5, decimal_places=2)
    Cantidad = models.IntegerField(blank=True, null=True)
    IVA = models.DecimalField(max_digits=5, decimal_places=2)
    Producto = models.ForeignKey('Inventario.Producto',on_delete=models.CASCADE)
    Venta = models.ForeignKey('Venta',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Producto} {self.Cantidad} {self.Subtotal}"
