from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """ Manager modelo Autor """
    
    def listar_autores(self):
        return self. all()
    
    def buscar_autores_solo_nombre(self, keyword):
        resultado = self.filter(nombre__icontains=keyword)
        return resultado
    
    def buscar_autores_nombre_o_apellido(self, keyword):
        resultado = self.filter(
                Q(nombre__icontains=keyword) | Q(apellido__icontains=keyword)
            )
        return resultado
    
    def buscar_autores_nombre_o_apellido_excluir_edad(self, keyword):
        """ Se puede concatenar los filtro o agregar exclusiones """
        resultado = self.filter(
                Q(nombre__icontains=keyword) | Q(apellido__icontains=keyword)
            ).exclude(edad__gte=42)
        return resultado