# Generated by Django 4.0.4 on 2022-06-21 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_alter_donacion_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='desc',
            field=models.IntegerField(default=0.05),
        ),
    ]