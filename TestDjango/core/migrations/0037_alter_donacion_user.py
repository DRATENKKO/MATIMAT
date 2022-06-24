# Generated by Django 4.0.4 on 2022-06-22 02:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0036_alter_donacion_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donacion',
            name='user',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
