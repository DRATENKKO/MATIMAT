# Generated by Django 4.0.4 on 2022-06-22 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_alter_donacion_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donacion',
            name='user',
        ),
    ]
