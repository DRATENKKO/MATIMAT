# Generated by Django 4.0.4 on 2022-06-21 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_alter_descuentodonacion_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descuentodonacion',
            name='id',
            field=models.IntegerField(default=True, primary_key=True, serialize=False),
        ),
    ]
