# Generated by Django 3.0.4 on 2020-12-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0021_auto_20201201_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honorarios',
            name='fecha',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización'),
        ),
    ]