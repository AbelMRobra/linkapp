# Generated by Django 3.0.4 on 2020-12-15 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0020_auto_20201201_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comparativas',
            name='fecha_autorizacion',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de aturorizacion'),
        ),
    ]
