# Generated by Django 4.0.4 on 2022-06-06 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_rename_correo_donacion_correo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='correo',
            field=models.EmailField(max_length=254),
        ),
    ]
