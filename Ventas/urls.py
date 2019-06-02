from django.contrib import admin
from django.urls import path

from .views import ProductoList,ProductoDetail,ProductoDetalle

urlpatterns = [
    path('catalogo/',ProductoList.as_view(),name="catalogo"),
#    path('producto/<slug:id>',ProductoDetail.as_view(),name="producto"),
    path('producto/<int:id>',ProductoDetalle,name="producto"),

]
