# Generated by Django 4.0.4 on 2022-06-26 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineapedido',
            name='user',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='user',
        ),
    ]