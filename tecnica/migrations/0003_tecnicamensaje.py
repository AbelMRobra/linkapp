# Generated by Django 3.0.4 on 2020-12-21 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0007_datosusuario_email'),
        ('tecnica', '0002_auto_20201216_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='TecnicaMensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(blank=True, max_length=200, null=True, verbose_name='Mensaje')),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fecha de creación')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tecnica.ItemEtapa', verbose_name='Item asociado')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrhh.datosusuario', verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
            },
        ),
    ]