# Generated by Django 3.0.4 on 2020-04-15 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0007_constantes_fecha_a'),
        ('compras', '0007_compras_precio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='compras',
            options={'verbose_name': 'Compra', 'verbose_name_plural': 'Compras'},
        ),
        migrations.CreateModel(
            name='Retiros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(verbose_name='Cantidad')),
                ('fecha_c', models.DateField(auto_now_add=True, verbose_name='Fecha de retiro')),
                ('fecha_a', models.DateField(auto_now=True, verbose_name='Fecha de actualización')),
                ('documento', models.CharField(max_length=200, verbose_name='Documento de referencia')),
                ('articulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presupuestos.Articulos', verbose_name='Articulo')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Compras', verbose_name='Compra')),
            ],
            options={
                'verbose_name': 'Retiro',
                'verbose_name_plural': 'Retiros',
            },
        ),
    ]
