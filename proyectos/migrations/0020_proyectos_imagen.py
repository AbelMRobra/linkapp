# Generated by Django 3.0.4 on 2021-01-26 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0019_proyectos_fecha_i'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagen del proyecto'),
        ),
    ]