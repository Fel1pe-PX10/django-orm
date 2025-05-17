

from django.urls import path

from . import views

app_name = 'autor_app'

urlpatterns = [
    path('autores/', views.ListAutores.as_view(), name='autores'),
]
