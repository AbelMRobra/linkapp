# Generated by Django 3.0.4 on 2020-06-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_pricing'),
    ]

    operations = [
        migrations.AddField(
            model_name='pricingresumen',
            name='base_precio',
            field=models.FloatField(blank=True, null=True, verbose_name='Base de precio'),
        ),
    ]
