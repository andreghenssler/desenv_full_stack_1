# Generated by Django 5.1.7 on 2025-05-10 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empregos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidato',
            name='escolaridade',
            field=models.CharField(choices=[('ENSINO_FUNDAMENTAL', 'Ensino Fundamental'), ('ENSINO_MEDIO', 'Ensino Médio'), ('SUPERIOR', 'Superior'), ('POS_GRADUACAO', 'Pós-Graduação'), ('MESTRADO', 'Mestrado'), ('DOUTORADO', 'Doutorado'), ('OUTRO', 'Outros')], max_length=20),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outros')], max_length=10),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='area',
            field=models.CharField(choices=[('TI', 'Tecnologia da Informação'), ('ENG', 'Engenharia'), ('ADM', 'Administração'), ('MKT', 'Marketing'), ('VEND', 'Vendas'), ('RH', 'Recursos Humanos'), ('FIN', 'Finanças'), ('JUR', 'Jurídico'), ('OUTRO', 'Outros')], max_length=20),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='tipo',
            field=models.CharField(choices=[('CLT', 'Consolidação das Leis do Trabalho'), ('PJ', 'Pessoa Jurídica'), ('EST', 'Estágio'), ('TRA', 'Treinamento'), ('OUTRO', 'Outros')], max_length=20),
        ),
    ]
