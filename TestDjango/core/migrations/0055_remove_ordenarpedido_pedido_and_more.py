# Generated by Django 4.0.4 on 2022-06-29 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_pedido_ordenarpedido_enviodireccion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordenarpedido',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='ordenarpedido',
            name='producto',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='user',
        ),
        migrations.DeleteModel(
            name='EnvioDireccion',
        ),
        migrations.DeleteModel(
            name='OrdenarPedido',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]
