# Generated by Django 3.0.4 on 2020-11-18 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0016_registroalmacenero_retiro_socios'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovimientoAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha del archivo')),
                ('archivo', models.FileField(upload_to='', verbose_name='Archivo')),
                ('estado', models.CharField(choices=[('ESPERA', 'Espera'), ('APROBADA', 'Aprobada'), ('RECHAZADA', 'Rechazada')], default='ACTIVA', max_length=20, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Movimiento de administración',
                'verbose_name_plural': 'Movimientos de administración',
            },
        ),
    ]
