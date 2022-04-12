from dataclasses import fields
from math import gcd
from multiprocessing import context
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from .models import Coche
from .models import Marca
from django.views.generic.edit import FormView
from applications.marca.models import  Marca
from applications.modelo.models import  Modelo
from .models import Coche

class InicioView(TemplateView):
    """Pagina de inicio"""
    template_name = 'inicio.html'

class ListAllCoches(ListView):
    template_name = 'coche/list_all.html'
    paginate_by = 4
    context_object_name = 'coches'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        print('========', palabra_clave)
        lista = Coche.objects.filter(
            #marca__name=palabra_clave
            matr__icontains=palabra_clave
        )
        return lista


class ListByMarca(ListView):
    template_name = 'coche/list_by_marca.html'

    def get_queryset(self):
        marca3=self.kwargs['marca2']
        lista = Coche.objects.filter(
        marca__name=marca3
        )
        return lista

class ListCochesByKword(ListView):
    template_name = 'coche/by_kword.html'
    context_object_name = 'marca'

    def get_queryset(self):
        print('******************')
        palabra_clave = self.request.GET.get("kword", '')
        print('========', palabra_clave)
        lista = Coche.objects.filter(
        marca__name=palabra_clave
        )
        return lista


class CocheDetailView(DetailView):
    model = Coche
    template_name = "coche/detail_coche.html"


class SuccessView(TemplateView):
    template_name = "coche/success.html"


class CocheCreateView(CreateView):
    template_name = "coche/add.html"
    model = Coche
    fields = ('__all__')
    success_url = reverse_lazy('coche_app:correcto')
    


class CocheUpdateView(UpdateView):
    template_name = "coche/update.html"
    model = Coche
    fields = ('__all__')
    success_url = reverse_lazy('coche_app:correcto')



class CocheDeleteView(DeleteView):
    model = Coche
    template_name = "coche/delete.html"
    success_url = reverse_lazy('coche_app:correcto')


    
class FiltrarPorFecha(ListView):
    template_name = 'coche/fecha.html'
    context_object_name = 'fecha'

    def get_queryset(self):
        print('******************')
        palabra_clave = self.request.GET.get("kword", '')
        print('========', palabra_clave)
        lista = Coche.objects.filter(
        fecha__name=palabra_clave
        )
        return lista
#class newCocheView(FormView):
#    template_name = 'coche/new_marca.html'
#    form_class = NewCocheForm
#    success_url = '/'













