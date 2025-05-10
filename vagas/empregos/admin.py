from django.contrib import admin
from .models import Vaga, Candidato

# Register your models here.
@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'area', 'tipo', 'salario', 'localizacao', 'data_publicacao')
    search_fields = ('titulo', 'area')
    list_filter = ('area', 'tipo')

@admin.register(Candidato)
class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'genero', 'escolaridade', 'data_cadastro')
    search_fields = ('nome', 'email')
    list_filter = ('genero', 'escolaridade')