# Generated by Django 3.0.4 on 2021-02-05 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0020_proyectos_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='numero_cuenta',
            field=models.IntegerField(blank=True, null=True, verbose_name='Numero de cuenta corriente'),
        ),
    ]
