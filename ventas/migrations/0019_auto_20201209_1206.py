# Generated by Django 3.0.4 on 2020-12-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0018_archivofechaentrega'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoVariacionHormigon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de carga')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='', verbose_name='archivo')),
            ],
            options={
                'verbose_name': 'Archivo Variacion Hormigon',
                'verbose_name_plural': 'Archivos Variacion Hormigon',
            },
        ),
        migrations.AlterModelOptions(
            name='archivofechaentrega',
            options={'verbose_name': 'Archivo Fecha de entrega', 'verbose_name_plural': 'Archivos Fecha de entrega'},
        ),
    ]