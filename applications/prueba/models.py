from django.db import models

# Create your models here.
class Persona(models.Model):
    """Model definition for Persona."""

    nombre_completo = models.CharField('Nombres', max_length=50)
    pais = models.CharField('Pais', max_length=50)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.PositiveIntegerField()
    apodo = models.CharField('Apodo', max_length=50)

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'persona'
        unique_together = ['pais', 'apodo']
        constraints = [
            models.CheckConstraint(check=models.Q(edad__gte=18), name='edad_mayor_o_igual_18')
        ]

    def __str__(self):
        """Unicode representation of Persona."""
        return f'{self.nombre_completo}'
