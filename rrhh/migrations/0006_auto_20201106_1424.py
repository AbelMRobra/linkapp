# Generated by Django 3.0.4 on 2020-11-06 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0005_auto_20201106_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notadepedido',
            name='visto',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Visto'),
        ),
    ]