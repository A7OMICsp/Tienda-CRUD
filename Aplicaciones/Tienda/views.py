from django.forms import RegexField
from django.shortcuts import render, redirect
from .models import Producto
import difflib

# Create your views here.

def home(request):
    ProductosListados = Producto.objects.all()
    return render(request, "home.html", {"productos": ProductosListados})

def gestionCursos(request):
    ProductosListados = Producto.objects.all()
    return render(request, "gestionCursos.html", {"productos": ProductosListados})

def registrarProducto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']
    descripcion = request.POST['txtDescripcion']

    producto = Producto.objects.create(codigo=codigo, nombre=nombre, precio=precio, descripcion=descripcion)
    return redirect('/gestionCursos/')

def edicionProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)

    return render(request, "edicionCurso.html", {"producto": producto})

def editarProducto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']
    descripcion = request.POST['txtDescripcion']

    producto = Producto.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.precio = precio
    producto.descripcion = descripcion
    producto.save()

    return redirect('/')

def eliminarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect('/gestionCursos/')

def visualizarProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)

    return render(request, "paginaProducto.html", {"producto": producto})

def buscarProducto(request):
    if request.method == "POST":
        txtBusqueda = request.POST['txtBusqueda']

        resultado = Producto.objects.filter(nombre__contains = txtBusqueda)
        
        return render(request, "resultadoBusqueda.html", {'txtBusqueda': txtBusqueda, 'resultado': resultado})
    else:
        return render(request, "resultadoBusqueda.html", {})

def paginaAyuda(request):

    return render(request, "ayuda.html")
    
