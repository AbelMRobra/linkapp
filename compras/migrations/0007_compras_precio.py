# Generated by Django 3.0.4 on 2020-04-15 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0006_compras_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='precio',
            field=models.FloatField(blank=True, null=True, verbose_name='Precio'),
        ),
    ]