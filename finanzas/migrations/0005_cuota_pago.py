# Generated by Django 3.0.4 on 2020-07-30 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0017_presupuestos_saldo_cap'),
        ('finanzas', '0004_cuentacorriente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de venta')),
                ('precio', models.FloatField(verbose_name='Precio de la cuota en moneda dura')),
                ('precio_pesos', models.FloatField(blank=True, null=True, verbose_name='Precio en pesos')),
                ('constante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='presupuestos.Constantes', verbose_name='Constante asociada')),
                ('cuenta_corriente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzas.CuentaCorriente', verbose_name='Cuenta corriente')),
            ],
            options={
                'verbose_name': 'Cuota',
                'verbose_name_plural': 'Cuotas',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha de venta')),
                ('pago', models.FloatField(verbose_name='Pago en moneda dura')),
                ('pago_pesos', models.FloatField(verbose_name='Pago en pesos')),
                ('documento_1', models.CharField(max_length=100, verbose_name='Documento 1')),
                ('documento_2', models.CharField(max_length=100, verbose_name='Documento 2')),
                ('cuota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanzas.Cuota', verbose_name='Cuota')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
            },
        ),
    ]
