# Generated by Django 3.0.4 on 2020-06-25 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0009_auto_20200612_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='unidades',
            name='sup_equiv',
            field=models.FloatField(blank=True, null=True, verbose_name='Sup. Equivalente'),
        ),
    ]
