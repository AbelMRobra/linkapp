# Generated by Django 3.0.4 on 2020-04-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0008_desde_pricing'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulos',
            name='id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]