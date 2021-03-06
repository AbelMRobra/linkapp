# Generated by Django 3.0.4 on 2020-08-05 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0016_proyectos_folleto'),
        ('finanzas', '0006_auto_20200731_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroAlmacenero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cheques_emitidos', models.FloatField(blank=True, null=True, verbose_name='Cheques emitidos')),
                ('gastos_fecha', models.FloatField(blank=True, null=True, verbose_name='Gastos a la fecha')),
                ('pendiente_admin', models.FloatField(blank=True, null=True, verbose_name='Pendiente de administración')),
                ('pendiente_comision', models.FloatField(blank=True, null=True, verbose_name='Pendiente de comisión')),
                ('pendiente_adelantos', models.FloatField(blank=True, null=True, verbose_name='Adelantos realizados')),
                ('pendiente_iva_ventas', models.FloatField(blank=True, null=True, verbose_name='IVA sobre ventas')),
                ('pendiente_iibb_tem', models.FloatField(blank=True, null=True, verbose_name='IIBB + TEM')),
                ('prestamos_proyecto', models.FloatField(blank=True, null=True, verbose_name='Prestamos a proyectos')),
                ('prestamos_otros', models.FloatField(blank=True, null=True, verbose_name='Prestamos a otros')),
                ('cuotas_cobradas', models.FloatField(blank=True, null=True, verbose_name='Cuotas cobradas')),
                ('cuotas_a_cobrar', models.FloatField(blank=True, null=True, verbose_name='Cuotas a cobrar')),
                ('ingreso_ventas', models.FloatField(blank=True, null=True, verbose_name='Ingreso por unidades a vender')),
                ('Prestamos_dados', models.FloatField(blank=True, null=True, verbose_name='Prestamos otorgados')),
                ('unidades_socios', models.FloatField(blank=True, editable=False, null=True, verbose_name='Unidades de Socios')),
                ('proyecto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyectos.Proyectos', verbose_name='Proyecto')),
            ],
            options={
                'verbose_name': 'RegistroAlmacenero',
                'verbose_name_plural': 'RegistroAlmaceneros',
            },
        ),
    ]
