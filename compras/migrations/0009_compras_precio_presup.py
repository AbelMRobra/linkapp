# Generated by Django 3.0.4 on 2020-05-28 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0008_auto_20200415_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='precio_presup',
            field=models.FloatField(blank=True, null=True, verbose_name='Precio de presupuesto'),
        ),
    ]
