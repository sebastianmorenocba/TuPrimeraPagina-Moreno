# Generated by Django 5.0.1 on 2024-02-08 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_estudiante_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursoestudiantes',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='cursoestudiantes',
            name='estudiante',
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('dominio', models.CharField(max_length=50)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.cliente')),
                ('mecanico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.mecanico')),
            ],
        ),
        migrations.CreateModel(
            name='VehiculoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vehiculo')),
            ],
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
        migrations.DeleteModel(
            name='CursoEstudiantes',
        ),
    ]
