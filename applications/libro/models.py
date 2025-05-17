from django.db import models

from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager

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
    
    class Meta:
        verbose_name = 'Libros'
        verbose_name_plural = 'Libros'
    
    objects = LibroManager()
    
    def __str__(self):
        return f'{self.titulo}'