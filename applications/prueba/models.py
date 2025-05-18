from django.db import models

# Create your models here.
class Persona(models.Model):
    """Model definition for Persona."""

    nombre_completo = models.CharField('Nombres', max_length=50, default='')
    pais = models.CharField('Pais', max_length=50, default='')
    pasaporte = models.CharField('Pasaporte', max_length=50, default='')
    edad = models.PositiveIntegerField(default=18)
    apodo = models.CharField('Apodo', max_length=50, default='')

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        # db_table = 'persona'
        models.UniqueConstraint(
            fields=['pais', 'apodo'],
            name='uniq_pais_apodo_%(app_label)s_%(class)s'
        ),
        constraints = [
            models.CheckConstraint(
                check=models.Q(edad__gte=18),
                name='edad_mayor_o_igual_18_%(app_label)s_%(class)s'
            )
        ]
        abstract = True

    def __str__(self):
        """Unicode representation of Persona."""
        return f'{self.nombre_completo}'
    
    
class Empleado(Persona):
    cargo = models.CharField('Cargo', max_length=50)
    

class Cliente(Persona):
    email = models.CharField('Email', max_length=50)
