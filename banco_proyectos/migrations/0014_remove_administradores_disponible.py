# Generated by Django 3.0.2 on 2020-02-26 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banco_proyectos', '0013_auto_20200226_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administradores',
            name='disponible',
        ),
    ]
