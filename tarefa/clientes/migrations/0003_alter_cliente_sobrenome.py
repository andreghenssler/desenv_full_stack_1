# Generated by Django 5.1.7 on 2025-04-21 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_sobrenome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(max_length=100),
        ),
    ]
