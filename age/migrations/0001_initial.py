# Generated by Django 3.0.4 on 2020-04-11 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('constantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('valor', models.FloatField()),
                ('valor_aux', models.FloatField(null=True)),
                ('descrip', models.TextField()),
                ('Unidad', models.CharField(blank=True, max_length=10)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('constante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='constantes.Constantes')),
            ],
            options={
                'verbose_name': 'Insumo',
                'verbose_name_plural': 'Insumos',
            },
        ),
    ]
