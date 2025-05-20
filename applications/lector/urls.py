

from django.urls import path

from . import views

app_name = 'lector_app'

urlpatterns = [
    path('registro-prestamo/', views.RegistrarPrestamo.as_view(), name='prestamo_registrar'),
    path('registro-prestamo-validacion/', views.RegistrarPrestamoValidacion.as_view(), name='prestamo_registrar_validacion'),
    path('registro-prestamo-multiple/', views.RegistrarPrestamoMultiple.as_view(), name='prestamo_registrar_multiple'),
]
