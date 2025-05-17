

import datetime

from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Libro


class ListLibros(ListView):
    template_name = "libro/list.html"
    context_object_name = 'libros'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('keyword', '')
        fecha_1 = self.request.GET.get('fecha1', '')
        fecha_2 = self.request.GET.get('fecha2', '')
         
        fecha_1 = datetime.datetime.strptime(fecha_1, '%Y-%m-%d').date() if fecha_1 != '' else datetime.datetime.strptime('1900-01-01', '%Y-%m-%d').date()
        fecha_2 = datetime.datetime.strptime(fecha_2, '%Y-%m-%d').date() if fecha_2 != '' else datetime.datetime.now().strftime('%Y-%m-%d')

        return Libro.objects.buscar_libros_rango_fecha(palabra_clave, fecha_1, fecha_2)


class ListLibrosTrigram(ListView):
    template_name = "libro/list.html"
    context_object_name = 'libros'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('keyword', '')
        return Libro.objects.listar_libros_trigram(palabra_clave)
    

class ListLibrosCategoria(ListView):
    template_name = "libro/list.html"
    context_object_name = 'libros'
    
    def get_queryset(self):
        categoria = self.kwargs['pk']
        return Libro.objects.buscar_libros_categoria(categoria)


class LibroDetail(DetailView):
    template_name = "libro/detalle.html"
    context_object_name = 'libro'

    def get_queryset(self):
        libro = self.kwargs['pk']
        return Libro.objects.all()