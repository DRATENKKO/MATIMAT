# Generated by Django 4.0.4 on 2022-06-25 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_remove_donacion_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donacion',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='donacion',
            name='desc',
        ),
    ]
