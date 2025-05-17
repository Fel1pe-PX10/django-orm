

from django.urls import path

from . import views

app_name = 'libro_app'

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='libros'),
    path('libros-trigram/', views.ListLibrosTrigram.as_view(), name='libros_trigram'),
    path('libros-categoria/<int:pk>', views.ListLibrosCategoria.as_view(), name='libros-categorias'),
    path('libro-detalle/<int:pk>', views.LibroDetail.as_view(), name='detalle'),
]
