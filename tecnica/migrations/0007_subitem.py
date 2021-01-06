# Generated by Django 3.0.4 on 2020-12-30 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0008_datosusuario_estado'),
        ('compras', '0021_auto_20201215_1202'),
        ('tecnica', '0006_auto_20201228_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre del subitem')),
                ('orden', models.FloatField(default=0.0, verbose_name='Orden')),
                ('estado', models.CharField(choices=[('ESPERA', 'Espera'), ('TRABAJANDO', 'Trabajando'), ('PROBLEMAS', 'Problemas'), ('LISTO', 'Listo')], default='ESPERA', max_length=20, verbose_name='Estado')),
                ('archivo_vigente', models.FileField(blank=True, null=True, upload_to='', verbose_name='Archivo vigente')),
                ('fecha_estimada_i', models.DateField(blank=True, null=True, verbose_name='Fecha estimada de iniciación')),
                ('fecha_estimada_f', models.DateField(blank=True, null=True, verbose_name='Fecha estimada de finalziación')),
                ('fecha_inicio', models.DateField(blank=True, null=True, verbose_name='Fecha de inicio')),
                ('fecha_final', models.DateField(blank=True, null=True, verbose_name='Fecha final')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL del servidor')),
                ('contrato', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.Contratos', verbose_name='Contrato')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tecnica.ItemEtapa', verbose_name='Item')),
                ('responsable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rrhh.datosusuario', verbose_name='Responsable')),
            ],
            options={
                'verbose_name': 'Sub item',
                'verbose_name_plural': 'Sub item',
            },
        ),
    ]