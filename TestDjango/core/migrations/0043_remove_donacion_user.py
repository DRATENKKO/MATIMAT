# Generated by Django 4.0.4 on 2022-06-22 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0042_donacion_user_alter_donacion_correo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donacion',
            name='user',
        ),
    ]
