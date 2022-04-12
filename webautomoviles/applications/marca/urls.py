from unicodedata import name
from django.contrib import admin
from django.urls import path

from . import views

app_name = "marca_app"

urlpatterns = [
    path(
        'add_marca/', views.MarcaCreateView.as_view(),
        name='marca_add'
        ),
]