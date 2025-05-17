from django.db import models
from .managers import AutorManager


# Create your models here.
class Autor(models.Model):
    nombre = models.CharField('autor', max_length=50)
    apellido = models.CharField('apellido', max_length=50)
    nacionalidad = models.CharField('nacionalidad', max_length=50)
    edad = models.PositiveIntegerField()
    
    objects = AutorManager()
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.nacionalidad}'