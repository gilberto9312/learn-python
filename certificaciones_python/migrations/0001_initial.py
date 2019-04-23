# Generated by Django 2.2 on 2019-04-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fechaInicio', models.DateTimeField()),
                ('fechaFin', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('fechaRegistro', models.DateTimeField(auto_now_add=True)),
                ('fechaActualizacion', models.DateTimeField(auto_now_add=True)),
                ('entidadesId', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
