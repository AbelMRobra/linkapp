# Generated by Django 3.0.4 on 2020-06-12 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0008_auto_20200607_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyectos',
            name='color',
            field=models.TextField(blank=True, null=True, verbose_name='Color del proyecto'),
        ),
        migrations.AddField(
            model_name='proyectos',
            name='iamgen',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Logo del proyecto'),
        ),
    ]
