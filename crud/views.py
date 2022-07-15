from django.shortcuts import  render, get_object_or_404
from django.http import HttpResponse
from .models import Producto, Marca
from .forms import ContactoForm, Productoform
# Create your views here.

def home(request):

    return render(request, 'crud/home.html')


def sobrenosotros(request):
    return render(request, 'crud/sobrenosotros.html')

def contacto(request):
    data = {
        'form': ContactoForm()

    }
    return render(request, 'crud/contacto.html',data)

def login(request):
    return render(request, 'crud/login.html')


def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'crud/productos.html',data)


def despacho(request):
    return render(request, 'crud/despacho.html')

def agregar_producto(request):
    
    data = {
        'form': Productoform()
    }

    if request.method == 'POST':
        formulario = Productoform(data=request.POST, files=request.FILES)
        if formulario.is_valid():
                formulario.save()
                data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
   
    return render(request, 'crud/producto/agregar.html',data)


def login1(request):
    return render(request, 'crud/login1.html')


def modificar_producto(request, id):
     

    return render(request,'crud/producto/modificar.html')
  
