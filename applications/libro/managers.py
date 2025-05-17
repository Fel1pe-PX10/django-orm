from django.db import models
from django.db.models import Count
from django.contrib.postgres.search import TrigramSimilarity

class LibroManager(models.Manager):
    
    def buscar_libros_rango_fecha(self, keyword, fecha_1, fecha_2):
        resultado = self.filter(
            titulo__icontains=keyword,
            fecha_lanzamiento__range = (fecha_1, fecha_2)
            )
        return resultado
    
    def buscar_libros_categoria(self, categoria):
        return self.filter(
            categoria__id = categoria
        ).order_by('titulo')
        
    def agregar_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        
        return libro
    
    def listar_libros_trigram(self, keyword):
        if keyword:
            resultado = self.filter(
                titulo__trigram_similar=keyword
                )
        else:
            resultado = self.all()[:10]
            
        return resultado
        
        
class CategoriaManager(models.Manager):
    
    def categoria_autor(self, autor_id):
        resultado = self.filter(
            categoria_libro__autores__id=autor_id
            ).distinct()
        return resultado
    
    def categorias_con_cantidad_libros(self):
        resultado = self.annotate(
            num_libros = Count('categoria_libro')
        )
          
        return resultado