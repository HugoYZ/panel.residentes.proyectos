# Generated by Django 3.0.2 on 2020-02-06 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banco_proyectos', '0005_datosresidente_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datosresidente',
            name='usuario',
        ),
    ]
