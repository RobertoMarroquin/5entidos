# Modulos  de Django
from django.contrib import admin
# Modulos De App
from .models import Producto, Proveedor, RegistroCompra
# Register your models here.

admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(RegistroCompra)
