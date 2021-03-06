# Generated by Django 3.0.4 on 2020-06-11 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0013_presupuestos_imprevisto'),
    ]

    operations = [
        migrations.AddField(
            model_name='presupuestos',
            name='credito',
            field=models.FloatField(blank=True, null=True, verbose_name='Credito'),
        ),
        migrations.AddField(
            model_name='presupuestos',
            name='fdr',
            field=models.FloatField(blank=True, null=True, verbose_name='Fdr'),
        ),
        migrations.AddField(
            model_name='presupuestos',
            name='saldo',
            field=models.FloatField(blank=True, null=True, verbose_name='Saldo del proyecto'),
        ),
    ]
