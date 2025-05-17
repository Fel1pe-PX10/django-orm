from django.db import models

from applications.libro.models import Libro
from .managers import PrestamoManager

# Create your models here.
class Lector(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=50)
    edad = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f'{self.nombre} {self.apellidos} - {self.nacionalidad}'
    
class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name='libro_prestamo')
    fecha_prestado = models.DateTimeField('Fecha Prestamo')
    fecha_devolucion = models.DateTimeField('Fecha Devolucion', blank=True, null=True)
    devuelto = models.BooleanField()
    
    objects = PrestamoManager()
    
    def __str__(self):
        return self.libro.titulo