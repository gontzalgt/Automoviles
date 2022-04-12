from re import template
from django.shortcuts import render
from django.views.generic.edit import FormView

from applications.coche.models import Coche
from applications.modelo.models import Modelo
from .models import Marca
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from .forms import NewCocheForm

class MarcaCreateView(CreateView):
    template_name = "marca/add2.html"
    model = Marca
    fields = ('__all__')
    success_url = reverse_lazy('coche_app:correcto')
    
