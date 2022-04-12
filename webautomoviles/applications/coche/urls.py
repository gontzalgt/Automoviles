from unicodedata import name
from django.contrib import admin
from django.urls import path

from . import views

app_name = "coche_app"

urlpatterns = [
    path(
        '', 
        views.InicioView.as_view(), 
        name='inicio'
    ),
    path(
        'listar-todo-coches/',
        views.ListAllCoches.as_view(),
        name='coches_all'
    ),
    path('list_by_marca/<marca2>', views.ListByMarca.as_view()),
    path('buscar_marca/',
     views.ListCochesByKword.as_view(),
     name='buscar_por_marca'
     ),
    path(
        'ver_coche/<pk>', views.CocheDetailView.as_view(),
        name='coche_detail'
        ),
    path(
        'add_coche/', views.CocheCreateView.as_view(),
        name='coche_add'
        ),
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name='correcto'
    ),
    path(
        'update_coche/<pk>', 
        views.CocheUpdateView.as_view(), 
        name='modificar_coche'
    ),
    path(
        'delete_coche/<pk>', 
        views.CocheDeleteView.as_view(), 
        name='eliminar_coche'
    ),
    path(
        'filtrar_fecha2', 
        views.FiltrarPorFecha.as_view(), 
        name='filtrar_fecha'
    ),
]