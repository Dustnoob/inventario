from django.contrib import admin
from inventarioApp.models import *
from django.contrib.auth.models import Permission

# Register your models here.

admin.site.register(Permission)

class Productomodel(admin.ModelAdmin):
    list_display = ['IdProducto','codigo','categoria','nombre','descripcion','stock','precio']
admin.site.register(Producto,Productomodel) 


