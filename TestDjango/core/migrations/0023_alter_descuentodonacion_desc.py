# Generated by Django 4.0.4 on 2022-06-21 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_donacion_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuentodonacion',
            name='desc',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
    ]