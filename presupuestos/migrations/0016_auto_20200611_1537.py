# Generated by Django 3.0.4 on 2020-06-11 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0015_presupuestos_anticipos'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuestos',
            name='saldo_mat',
            field=models.FloatField(blank=True, null=True, verbose_name='Saldo del proyecto - Materiales'),
        ),
        migrations.AddField(
            model_name='presupuestos',
            name='saldo_mo',
            field=models.FloatField(blank=True, null=True, verbose_name='Saldo del proyecto - Mano de obra'),
        ),
    ]
