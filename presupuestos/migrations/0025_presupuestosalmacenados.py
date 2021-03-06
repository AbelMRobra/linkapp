# Generated by Django 3.0.4 on 2021-04-22 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0023_auto_20210302_0909'),
        ('presupuestos', '0024_auto_20210407_0946'),
    ]

    operations = [
        migrations.CreateModel(
            name='PresupuestosAlmacenados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('archivo', models.FileField(upload_to='', verbose_name='Archivo')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.Proyectos', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'Almacen',
                'verbose_name_plural': 'Almacenes',
            },
        ),
    ]
