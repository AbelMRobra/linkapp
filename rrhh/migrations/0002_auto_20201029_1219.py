# Generated by Django 3.0.4 on 2020-10-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosusuario',
            name='imagenlogo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='datosusuario',
            name='imagen',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True, verbose_name='Imagen'),
        ),
    ]