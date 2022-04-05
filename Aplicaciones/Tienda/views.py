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

    producto = Producto.objects.create(codigo=codigo, nombre=nombre, precio=precio)
    return redirect('/gestionCursos/')

def edicionProducto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)

    return render(request, "edicionCurso.html", {"producto": producto})

def editarProducto(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    precio = request.POST['numPrecio']

    producto = Producto.objects.get(codigo=codigo)
    producto.nombre = nombre
    producto.precio = precio
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
    productos = Producto.objects.all()
    nombre = request.POST['txtBusqueda']
    difflib.get_close_matches(nombre, productos.nombre)
    
    return render(request, "gestionCursos2.html", {"productos": productos})
