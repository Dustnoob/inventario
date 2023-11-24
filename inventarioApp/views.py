from django.shortcuts import render, redirect
from .models import Producto
from . import forms
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductoSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

@permission_required('inventarioApp.add_producto')
# VIEWS PRODUCTO
@login_required
def index(request):
    return render(request, 'index.html')

# Views listado de productos

@login_required
def listadoGventas(request):
    producto = Producto.objects.all()
    data = {'producto': producto}
    return render(request, 'gventas.html')


@login_required
def listadoProducto(request):
    producto = Producto.objects.all()
    data = {'producto': producto}
    return render(request, 'list.html', data)


@login_required
def agregarProducto(request):
    form = forms.RegistroProductoForm()
    if request.method == 'POST':
        form = forms.RegistroProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return listadoProducto(request)
    data = {'form': form}
    return render(request, 'agregar.html', data)


@login_required
def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('/producto', request)


@login_required
def actualizarProducto(request, id):
    producto = Producto.objects.get(id=id)
    form = forms.RegistroProductoForm(instance=producto)
    if request.method == 'POST':
        form = forms.RegistroProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return listadoProducto(request)
    data = {'form': form}
    return render(request, 'agregar.html', data)



@api_view(['GET', 'POST'])
def producto_list(request):
    if request.method == 'GET':
        producto = Producto.objects.all().order_by("fecha")
        ser = ProductoSerializer(Producto, many=True)
        return Response(ser.data)

    if request.method == 'POST':
        ser = ProductoSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def producto_detail(request, pk):
    try:
        producto = Producto.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ser = ProductoSerializer(producto)
        return Response(ser.data)
    if request.method == 'PUT':
        ser = ProductoSerializer(producto, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)