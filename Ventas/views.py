#Modulos Django
from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,DetailView
from django.contrib.auth.decorators import login_required

#Python Librerias

#Librerias de App
from .models import Venta,LineaVenta
from Inventario.models import Producto

class ProductoList(ListView):
    model = Producto
    pagination = 10
    template_name = "Catalogo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ProductoDetail(DetailView):
    model = Producto
    template_name = "productoDetalle.html"
    slug_field = "id"
    slug_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@login_required
def ProductoDetalle(request,id):
    context = {}
    producto = Producto.objects.get(id=id)
    print(producto.Cantidad)
    context.update({"object":producto})
    if request.method == "POST":
        cantidad = int(request.POST["cantidad"])
        print(cantidad)
        precio = request.POST['precio']
        producto.Cantidad = producto.Cantidad - cantidad
        producto.save()
        
        venta=Venta.objects.create()
        venta.save()

        lineaventa = LineaVenta.objects.create(Subtotal=precio,Cantidad=cantidad,IVA=cantidad*1.13,Producto=producto,Venta=venta)
        lineaventa.save()

        return redirect("ventas:catalogo")
    return render(request,'productoDetalle.html',context)
