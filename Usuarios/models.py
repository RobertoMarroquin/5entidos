#Modulo Django
from django.db import models
from django.contrib.auth.models import User

#Modulos Python
import datetime

#Create your models here.

class Usuario(models.Model):
    """(Usuario description)"""

    usuario = models.OneToOneField(User,blank=False,null=False,on_delete=models.CASCADE)
    nombres = models.CharField(blank=True, max_length=100)
    apellidos = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
