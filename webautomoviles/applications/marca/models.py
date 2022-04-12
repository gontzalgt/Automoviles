from django.db import models

# Create your models here.
class Marca(models.Model):
    name = models.CharField('Marca', max_length=50)
    sede = models.CharField('Sede', max_length=50, blank=True)

    def __str__(self):
        return self.name