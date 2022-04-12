from unicodedata import name
from django.contrib import admin
from django.urls import path

from . import views

app_name = "modelo_app"

urlpatterns = [
    path(
        'add_modelo/', views.ModeloCreateView.as_view(),
        name='modelo_add'
        ),
]