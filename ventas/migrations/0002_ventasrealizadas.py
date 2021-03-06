# Generated by Django 3.0.4 on 2020-05-06 20:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_auto_20200420_1150'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VentasRealizadas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprador', models.CharField(max_length=100, verbose_name='Nombre del comprador')),
                ('fecha', models.DateField(verbose_name='Fecha de venta')),
                ('tipo_venta', models.CharField(blank=True, choices=[('VENTA', 'Venta'), ('CANJE', 'Canje')], max_length=20, null=True, verbose_name='Tipo de venta')),
                ('unidad', models.CharField(max_length=100, verbose_name='Unidad')),
                ('tipo_unidad', models.CharField(blank=True, choices=[('DTO', 'Dto'), ('COCHERA', 'Cochera')], max_length=20, null=True, verbose_name='Tipo de unidad')),
                ('asignacion', models.CharField(max_length=100, verbose_name='Asignacion')),
                ('m2', models.FloatField(verbose_name='Metros cuadrados')),
                ('precio_venta', models.FloatField(verbose_name='Precio de venta')),
                ('anticipo', models.FloatField(verbose_name='Anticipo')),
                ('cuotas_pend', models.IntegerField(verbose_name='Cuotas pendientes')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.Proyectos', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
    ]
