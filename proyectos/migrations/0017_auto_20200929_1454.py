# Generated by Django 3.0.4 on 2020-09-29 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0016_proyectos_folleto'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidades',
            name='estado_comision',
            field=models.CharField(blank=True, choices=[('SI', 'Si'), ('NO', 'No')], default='NO', max_length=20, null=True, verbose_name='Estado de comision'),
        ),
        migrations.AddField(
            model_name='unidades',
            name='estado_iibb',
            field=models.CharField(blank=True, choices=[('SI', 'Si'), ('NO', 'No')], default='NO', max_length=20, null=True, verbose_name='Estado de IIBB'),
        ),
    ]