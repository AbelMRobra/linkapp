# Generated by Django 3.0.4 on 2021-06-02 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0024_auto_20210510_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='precio_linkp',
            field=models.FloatField(blank=True, null=True, verbose_name='Precio Link-P'),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='precio_posta',
            field=models.FloatField(blank=True, null=True, verbose_name='Precio posta'),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='precio_pricing',
            field=models.FloatField(blank=True, null=True, verbose_name='Precio Pricing'),
        ),
    ]
