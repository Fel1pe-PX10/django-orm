# Generated by Django 5.2.1 on 2025-05-17 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('fecha_lanzamiento', models.DateField(verbose_name='Fecha Lanzamiento')),
                ('portada', models.ImageField(blank=True, null=True, upload_to='portadas', verbose_name='Portada')),
                ('visitas', models.PositiveIntegerField()),
                ('autores', models.ManyToManyField(to='autor.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.categoria')),
            ],
        ),
    ]
