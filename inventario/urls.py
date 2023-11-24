"""
URL configuration for inventario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from inventarioApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
#    path("gventas/", views.listadoGventas),
#    path("gventas/agregar/", views.agregarGventas),
#    path("gventas/eliminar/<int:id>", views.eliminarGventas),
#    path("gventas/actualizar/<int:id>", views.actualizarGventas),
#    path("gventas/productoapi/", views.gventas_list),
#    path("gventas/productoapi/<int:pk>", views.gventas_detail),
    path('producto/',views.listadoProducto),
    path('agregar/', views.agregarProducto),
    path('eliminar/<int:id>', views.eliminarProducto),
    path('actualizar/<int:id>', views.actualizarProducto),
    path('productoapi/', views.producto_list),
    path('productoapi/<int:pk>', views.producto_detail),
    path('accounts/', include('django.contrib.auth.urls')),
#    path('chatbot/', views.chatbot),
 ]
