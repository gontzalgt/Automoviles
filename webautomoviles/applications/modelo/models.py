from django.db import models

# Create your models here.
class Modelo(models.Model):
    modelo = models.CharField('Modelo', max_length=50)
    serie = models.CharField('Nº serie', max_length=50, blank=True)

    def __str__(self):
        return self.modelo