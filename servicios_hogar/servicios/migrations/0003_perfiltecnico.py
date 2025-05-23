# Generated by Django 5.2 on 2025-04-21 04:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('servicios', '0002_notificacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilTecnico',
            fields=[
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='perfil_tecnico', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('especialidades', models.CharField(blank=True, max_length=255)),
                ('experiencia', models.TextField(blank=True)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
    ]
