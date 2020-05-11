# Generated by Django 3.0.4 on 2020-04-14 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0002_auto_20200414_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Desde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_costo', models.FloatField(blank=True, null=True, verbose_name='Valor de costo')),
                ('valor_costo_usd', models.FloatField(blank=True, null=True, verbose_name='Valor de costo en USD')),
                ('valor_final', models.FloatField(blank=True, null=True, verbose_name='Valor final')),
                ('valor_final_usd', models.FloatField(blank=True, null=True, verbose_name='Valor final en USD')),
                ('parametros', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presupuestos.Prametros', verbose_name='Parametros')),
            ],
            options={
                'verbose_name': 'Indicador de precio',
                'verbose_name_plural': 'Indicador de precios',
            },
        ),
    ]