# Generated by Django 4.0.4 on 2022-06-05 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_donacion_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donacion',
            old_name='idDonante',
            new_name='idDonacion',
        ),
        migrations.RenameField(
            model_name='donacion',
            old_name='donacion',
            new_name='valordonacion',
        ),
        migrations.RemoveField(
            model_name='donacion',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='donacion',
            name='nombreD',
        ),
        migrations.RemoveField(
            model_name='donacion',
            name='telefono',
        ),
    ]