# Generated by Django 3.0.4 on 2021-05-12 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0038_sugerencia_fecha_listo'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrocontable',
            name='caja',
            field=models.CharField(blank=True, default='Personal', max_length=400, null=True, verbose_name='Caja'),
        ),
        migrations.AddField(
            model_name='registrocontable',
            name='creador',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Creador'),
        ),
    ]
