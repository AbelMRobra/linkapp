# Generated by Django 3.0.4 on 2021-01-27 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0015_auto_20210108_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300, verbose_name='Nombre del anuncio')),
                ('descrip', models.CharField(max_length=300, verbose_name='Descripción corta')),
                ('imagen', models.ImageField(upload_to='', verbose_name='Imagen')),
                ('categoria', models.CharField(choices=[('LINKP', 'Linkp'), ('COMUNIDAD', 'Comunidad'), ('PROYECTOS', 'Proyectos')], max_length=20, verbose_name='Categoria')),
                ('activo', models.CharField(choices=[('SI', 'Si'), ('NO', 'No')], max_length=20, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Anuncio',
                'verbose_name_plural': 'Anuncios',
            },
        ),
    ]
