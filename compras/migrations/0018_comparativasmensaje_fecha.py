# Generated by Django 3.0.4 on 2020-10-29 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0017_comparativasmensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='comparativasmensaje',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación'),
        ),
    ]
