#Modulos django
from django.forms import ModelForm
#Modulos de App
from .models import Venta,LineaVenta


class CreateVentaEmpleado(ModelForm):
    """docstring for CreateVenta."""

    class Meta:
        model = Venta
        field = [""]
