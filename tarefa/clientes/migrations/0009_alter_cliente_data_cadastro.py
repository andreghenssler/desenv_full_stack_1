# Generated by Django 5.1.7 on 2025-04-21 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_alter_cliente_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
