# Modulos de Django
from django.contrib import admin
# Modulos de App
from .models import LineaVenta, Venta
# Register your models here.

admin.site.register(LineaVenta)
admin.site.register(Venta)
