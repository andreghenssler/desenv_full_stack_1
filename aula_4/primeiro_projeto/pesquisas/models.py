<<<<<<< HEAD
from django.db import models

# Create your models here.
class Questao(models.Model):
    texto_questao = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField("date published")

    def __str__(self):
        return self.texto_questao


class Alternativa(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    texto_alternativa = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    
    def __str__(self):
=======
from django.db import models

# Create your models here.
class Questao(models.Model):
    texto_questao = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField("date published")

    def __str__(self):
        return self.texto_questao


class Alternativa(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    texto_alternativa = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)
    
    def __str__(self):
>>>>>>> d4f1ef3 (Aula 16-04)
       return self.texto_alternativa