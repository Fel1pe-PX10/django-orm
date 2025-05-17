from django.shortcuts import render
from django.views.generic import ListView

from .models import Autor
# Create your views here.


class ListAutores(ListView):
    template_name = "autor/list.html"
    context_object_name = 'autores'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('keyword', '')
        return Autor.objects.buscar_autores_nombre_o_apellido_excluir_edad(palabra_clave)

    