# Generated by Django 3.0.4 on 2020-06-07 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0006_proyectos_desde'),
        ('ventas', '0003_estudiomercado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frente', models.CharField(choices=[('SI', 'Si'), ('NO', 'No')], max_length=20, verbose_name='Frente')),
                ('piso_intermedio', models.CharField(choices=[('SI', 'Si'), ('NO', 'No')], max_length=20, verbose_name='Piso intermedio')),
                ('cocina_separada', models.CharField(choices=[('SI', 'Si'), ('NO', 'No')], max_length=20, verbose_name='Cocina Separada')),
                ('local', models.CharField(choices=[('SI', 'Si'), ('NO', 'No')], max_length=20, verbose_name='Local Comercial')),
                ('menor_50_m2', models.CharField(choices=[('SI', 'Si'), ('NO', 'No')], max_length=20, verbose_name='Menor a 50 m2')),
                ('unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.Unidades', verbose_name='Unidades')),
            ],
            options={
                'verbose_name': 'Pricing por unidad',
                'verbose_name_plural': 'Pricing por unidades',
            },
        ),
    ]