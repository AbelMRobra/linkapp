# Generated by Django 3.0.4 on 2021-06-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0027_auto_20210625_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='flujo_ingreso',
            field=models.TextField(blank=True, null=True, verbose_name='Fluejo de ingreso'),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='flujo_ingreso_link',
            field=models.TextField(blank=True, null=True, verbose_name='Fluejo de ingreso de Link'),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='flujo_ingreso_proyecto',
            field=models.TextField(blank=True, null=True, verbose_name='Fluejo de ingreso de Proyecto'),
        ),
    ]
