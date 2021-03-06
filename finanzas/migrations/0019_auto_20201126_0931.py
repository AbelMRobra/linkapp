# Generated by Django 3.0.4 on 2020-11-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0018_auto_20201118_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuota',
            name='boleto',
            field=models.CharField(choices=[('BOLETO', 'Boleto'), ('NO BOLETO', 'No Boleto')], default='NO BOLETO', max_length=20, verbose_name='Boleto'),
        ),
        migrations.AddField(
            model_name='cuota',
            name='porc_boleto',
            field=models.FloatField(blank=True, null=True, verbose_name='Porcentaje a aplicar boleto'),
        ),
    ]
