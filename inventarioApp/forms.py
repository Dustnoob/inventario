from django import forms
from inventarioApp.models import Producto
from inventarioApp.models import Usuario

# Registro Producto

class RegistroProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields='__all__'
    CATEGORIA=[
        ('detergente', 'DETERGENTE'),
        ('bebida', 'BEBIDAS'),
        ('abarrotes', 'ABARROTES'),
    ]

    IdProducto = forms.IntegerField()
    codigo = forms.IntegerField()
    categoria=forms.CharField(widget=forms.Select(choices=CATEGORIA))
    nombre = forms.CharField()
    descripcion = forms.CharField()
    stock = forms.IntegerField(max_value=99)
    precio = forms.IntegerField()

    # Validación de campos a nivel frontend
    
    IdProducto.widget.attrs['class']='form-control'
    codigo.widget.attrs['class']='form-control'
    categoria.widget.attrs['class']='form-control'
    nombre.widget.attrs['class']='form-control'
    descripcion.widget.attrs['class']='form-control'
    stock.widget.attrs['class']='form-control'
    precio.widget.attrs['class']='form-control'

    def __str__(self):
        return self.nombre
        

class RegistroUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario # nombre del modelo dentro de models
        fields='__all__'
    nombre=forms.CharField()
    producto=forms.ModelChoiceField(queryset=Producto.objects.all().values('nombre'))
    
    nombre.widget.attrs['class']='form-control'
    producto.widget.attrs['class']='form-control'