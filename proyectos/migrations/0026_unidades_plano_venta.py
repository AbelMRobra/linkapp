# Generated by Django 3.0.4 on 2021-06-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0025_auto_20210602_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidades',
            name='plano_venta',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Adjunto'),
        ),
    ]
