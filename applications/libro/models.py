from django.db import models
from django.db.models.signals import post_save

from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager
from .signals import *

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField('Categoria', max_length=30)
    
    objects = CategoriaManager()
    
    def __str__(self):
        return f'{self.id} - {self.nombre}'
    
class Libro(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='categoria_libro')
    titulo = models.CharField('Titulo', max_length=50)
    autores = models.ManyToManyField(Autor)
    fecha_lanzamiento = models.DateField('Fecha Lanzamiento', auto_now=False, auto_now_add=False)
    portada = models.ImageField('Portada', upload_to='portadas', blank=True, null=True)
    visitas = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    
    class Meta:
        verbose_name = 'Libros'
        verbose_name_plural = 'Libros'
        
    @property
    def disminuir_stock(self):
        self.stock -= 1
        self.save()
    
    objects = LibroManager()
    
    def __str__(self):
        return f'{self.titulo}'
    
# Usando signals se pueden disparar o usar triggers dependiendo el evento ejecutado en la base de datos
# este es para reducir la imagen al 50%
post_save.connect(optimizar_imagen, sender=Libro)