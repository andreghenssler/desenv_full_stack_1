from django.db import models

# Create your models here.
Area_choices = [
    ('TI', 'Tecnologia da Informação'),
    ('ENG', 'Engenharia'),
    ('ADM', 'Administração'),
    ('MKT', 'Marketing'),
    ('VEND', 'Vendas'),
    ('RH', 'Recursos Humanos'),
    ('FIN', 'Finanças'),
    ('JUR', 'Jurídico'),
    ('OUTRO', 'Outros'),
]

Tipo_choices = [
    ('CLT', 'Consolidação das Leis do Trabalho'),
    ('PJ', 'Pessoa Jurídica'),
    ('EST', 'Estágio'),
    ('TRA', 'Treinamento'),
    ('OUTRO', 'Outros'),
]
Genero_choices = [
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outros'),
]

Escolaridade_choices = [
    ('ENSINO_FUNDAMENTAL', 'Ensino Fundamental'),
    ('ENSINO_MEDIO', 'Ensino Médio'),
    ('SUPERIOR', 'Superior'),
    ('POS_GRADUACAO', 'Pós-Graduação'),
    ('MESTRADO', 'Mestrado'),
    ('DOUTORADO', 'Doutorado'),
    ('OUTRO', 'Outros')
]
class Vaga(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    area = models.CharField(max_length=20, choices=Area_choices)
    tipo = models.CharField(max_length=20, choices=Tipo_choices)
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    localizacao = models.CharField(max_length=100)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    genero = models.CharField(max_length=10, choices=Genero_choices)
    escolaridade = models.CharField(max_length=20, choices=Escolaridade_choices)
    
    data_nascimento = models.DateField()
    experiencia = models.TextField()
    data_cadastro = models.DateTimeField(auto_now_add=True)
    # vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
