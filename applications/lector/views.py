from datetime import date

from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .models import Prestamo

from .forms import PrestamoForm, PrestamoMultipleForm
# Create your views here.

class RegistrarPrestamo(FormView):
    template_name = 'lector/prestamo/registrar.html'
    form_class = PrestamoForm
    success_url = '.'
    
    def form_valid(self, form):
        
        # Method 1
        # Prestamo.objects.create(
        #     lector = form.cleaned_data['lector'],
        #     libro = form.cleaned_data['libro'],
        #     fecha_prestado = date.today(),
        #     devuelto = False
        # )
        
        # Method 2
        prestamo = Prestamo(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestado = date.today(),
            devuelto = False
        )
        prestamo.save()
        
        # libro = form.cleaned_data['libro']
        # libro.stock -= 1
        # libro.save()
        
        return super(RegistrarPrestamo, self).form_valid(form)
    
    
class RegistrarPrestamoValidacion(FormView):
    template_name = 'lector/prestamo/registrar.html'
    form_class = PrestamoForm
    success_url = '.'
    
    def form_valid(self, form):
        
        obj, created = Prestamo.objects.get_or_create(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            devuelto = False,
            defaults={
                'fecha_prestado': date.today(),
            }
        )
        
        if created:
            return super(RegistrarPrestamoValidacion, self).form_valid(form)
        
        return HttpResponseRedirect(reverse_lazy('libro_app:libros'))
    
    
class RegistrarPrestamoMultiple(FormView):
    template_name = 'lector/prestamo/registrar_multiple.html'
    form_class = PrestamoMultipleForm
    success_url = '.'
    
    def form_valid(self, form):
        
        print('==============')
        print(form.cleaned_data['lector'])
        print(form.cleaned_data['libros'])
        
        librosPrestamo = []
        for libro in form.cleaned_data['libros']:
            prestamo = Prestamo(
                lector = form.cleaned_data['lector'],
                libro = libro,
                fecha_prestado = date.today(),
                devuelto = False
            )
            libro.disminuir_stock
            librosPrestamo.append(prestamo)
            
        Prestamo.objects.bulk_create(
            librosPrestamo
        )
            
        
        return HttpResponseRedirect(reverse_lazy('libro_app:libros'))