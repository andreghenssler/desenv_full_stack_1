<<<<<<< HEAD
# Generated by Django 5.1.7 on 2025-04-02 23:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_questao', models.CharField(max_length=200)),
                ('data_publicacao', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_alternativa', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pesquisas.questao')),
            ],
        ),
    ]
=======
# Generated by Django 5.1.7 on 2025-04-02 23:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_questao', models.CharField(max_length=200)),
                ('data_publicacao', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_alternativa', models.CharField(max_length=200)),
                ('votos', models.IntegerField(default=0)),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pesquisas.questao')),
            ],
        ),
    ]
>>>>>>> d4f1ef3 (Aula 16-04)
