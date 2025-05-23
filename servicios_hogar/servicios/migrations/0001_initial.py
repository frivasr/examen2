# Generated by Django 5.2 on 2025-04-21 03:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('direccion', models.CharField(max_length=255)),
                ('fecha_solicitud', models.DateTimeField(auto_now_add=True)),
                ('fecha_preferida', models.DateField()),
                ('estado', models.CharField(default='pendiente', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes', to=settings.AUTH_USER_MODEL)),
                ('tecnico_asignado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='asignaciones', to=settings.AUTH_USER_MODEL)),
                ('tipo_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servicios.tiposervicio')),
            ],
        ),
        migrations.CreateModel(
            name='CalificacionServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntuacion', models.IntegerField(choices=[(1, '1 estrella'), (2, '2 estrellas'), (3, '3 estrellas'), (4, '4 estrellas'), (5, '5 estrellas')])),
                ('comentario', models.TextField(blank=True)),
                ('fecha_calificacion', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('solicitud', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='calificacion', to='servicios.solicitudservicio')),
            ],
            options={
                'unique_together': {('solicitud', 'cliente')},
            },
        ),
    ]
