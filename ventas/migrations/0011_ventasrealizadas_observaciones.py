# Generated by Django 3.0.4 on 2020-07-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0010_auto_20200629_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='ventasrealizadas',
            name='observaciones',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
    ]
