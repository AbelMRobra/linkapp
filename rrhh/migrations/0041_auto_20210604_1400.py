# Generated by Django 3.0.4 on 2021-06-04 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0040_auto_20210602_0859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seguimiento',
            name='area',
            field=models.CharField(choices=[('PRESUPUESTOS', 'Presupuesto'), ('COMPRAS Y CONTRATACIONES', 'Compras Contrataciones'), ('EQUIPO TECNICO', 'Equipo Tecnico'), ('ADMINISTRACIÓN Y FINANZAS', 'Administracion Finanzas'), ('COMERCIALIZACIÓN Y MARKETING', 'Comercializacion Marketing'), ('RECURSOS HUMANOS', 'Rr Hh'), ('DIRECCIÓN', 'Direccion'), ('OBRA', 'Obra'), ('PRODUCCIÓN', 'Produccion'), ('ADMINISTRACIÓN', 'Administracion'), ('COMERCIALIZACIÓN', 'Comercializacion')], max_length=100, verbose_name='Area'),
        ),
    ]
