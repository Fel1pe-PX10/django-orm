from django.db import models

from django.db.models import Avg, Sum, Count
from django.db.models.functions import Lower


class PrestamoManager(models.Manager):
    
    def promedio_edad_lectores_libro(self):
        resultado = self.filter(
            libro__id = 1
        ).aggregate(
            promedio_edad = Avg('lector__edad'),
            suma_edades = Sum('lector__edad')
        )
        
        return resultado
    
    def cantidad_veces_libro_prestado(self):
        resultado = self.values(
            'libro'
        ).annotate(
            libro_veces = Count('libro'),
            titulo = Lower('libro__titulo')
        )
        
        for r in resultado:
            print(r)
        
        return resultado