# Generated by Django 4.0.4 on 2022-06-23 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_rename_nombrecompleto_donacion_nombredonante_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Donacion',
        ),
    ]
