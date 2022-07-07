# Generated by Django 4.0.4 on 2022-07-06 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pedidos', '0007_alter_enviodireccion_pedido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enviodireccion',
            name='pedido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido'),
        ),
        migrations.AlterField(
            model_name='enviodireccion',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]