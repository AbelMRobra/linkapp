# Generated by Django 3.0.4 on 2020-11-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0015_retirodesocios_proyecto'),
    ]

    operations = [
        migrations.AddField(
            model_name='registroalmacenero',
            name='retiro_socios',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Retiro socios'),
        ),
    ]
