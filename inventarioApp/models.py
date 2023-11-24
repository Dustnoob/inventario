from django.db import models
#from django.contrib.auth import Usuario
# Create your models here.

class Producto(models.Model):
    IdProducto = models.IntegerField(max_length=6)
    codigo = models.IntegerField(max_length=50)
    categoria = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    stock = models.IntegerField(max_length=6)
    precio = models.IntegerField(max_length=6)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    producto = models.ForeignKey('Producto', on_delete=models.SET_NULL, null=True) 
