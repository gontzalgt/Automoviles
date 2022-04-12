from re import template
from django.shortcuts import render
from django.views.generic.edit import FormView

from applications.coche.models import Coche
from applications.modelo.models import Modelo
from .models import Modelo
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

class ModeloCreateView(CreateView):
    template_name = "modelo/add3.html"
    model = Modelo
    fields = ('__all__')
    success_url = reverse_lazy('modelo_app:correcto')
    
