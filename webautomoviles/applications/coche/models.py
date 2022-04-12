from django.db import models

from applications.marca.models import Marca
from applications.modelo.models import Modelo

# Create your models here.
class Coche(models.Model):
    matr = models.CharField('Matricula', max_length=50)
    fecha = models.DateField('Fecha de creacion')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Mis coches'
        verbose_name_plural = 'Mis coches'

    def __str__(self):
        return str(self.id) + '-' + self.matr + '-' + str(self.fecha)