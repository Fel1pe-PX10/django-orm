# Generated by Django 5.2.1 on 2025-05-18 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0005_alter_lector_apellido_alter_lector_edad_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lector',
            options={'verbose_name': 'Lector', 'verbose_name_plural': 'Lectores'},
        ),
    ]
