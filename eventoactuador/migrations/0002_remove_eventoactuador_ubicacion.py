# Generated by Django 4.2.13 on 2025-06-08 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventoactuador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventoactuador',
            name='ubicacion',
        ),
    ]
