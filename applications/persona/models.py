from django.db import models

# Create your models here.
class Persona(models.Model):
    
    nombre = models.CharField('autor', max_length=50)
    apellido = models.CharField('apellido', max_length=50)
    nacionalidad = models.CharField('nacionalidad', max_length=50)
    edad = models.PositiveIntegerField()
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return f'{self.nombre} {self.apellido} - {self.nacionalidad}'