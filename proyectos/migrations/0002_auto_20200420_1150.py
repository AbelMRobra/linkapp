# Generated by Django 3.0.4 on 2020-04-20 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyectos',
            name='m2',
            field=models.FloatField(verbose_name='Tamaño de la obra'),
        ),
    ]
