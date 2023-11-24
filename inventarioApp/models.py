from django.db import models
#from django.contrib.auth import usuario
# Create your models here.

class Producto(models.Model):
    IdProducto = models.IntegerField()
    codigo = models.IntegerField()
    categoria = models.CharField()
    nombre = models.CharField()
    descripcion = models.CharField()
    stock = models.IntegerField()
    precio = models.IntegerField()

class Usuario(models.Model):
    nombre = models.CharField()
    producto = models.ForeignKey(
    'Producto', on_delete=models.SET_NULL, null=True ) 
