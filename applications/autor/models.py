from applications.persona.models import Persona
from .managers import AutorManager


# Create your models here.
class Autor(Persona):
    objects = AutorManager()