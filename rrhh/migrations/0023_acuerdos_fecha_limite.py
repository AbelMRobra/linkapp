# Generated by Django 3.0.4 on 2021-02-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0022_acuerdos_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='acuerdos',
            name='fecha_limite',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha limite'),
        ),
    ]
