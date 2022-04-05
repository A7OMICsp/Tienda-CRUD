from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('gestionCursos/', views.gestionCursos),
    path('registrarProducto/', views.registrarProducto),
    path('edicionProducto/<codigo>', views.edicionProducto),
    path('editarProducto/', views.editarProducto),
    path('eliminarProducto/<codigo>', views.eliminarProducto),
    path('paginaProducto/<codigo>', views.visualizarProducto),
    path('buscarProducto/', views.buscarProducto),
]