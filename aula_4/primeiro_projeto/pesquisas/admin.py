from django.contrib import admin
# Register your models here.

from .models import Questao, Alternativa

@admin.register(Questao)
class QuestaoAdmin(admin.ModelAdmin):
    list_display = ("texto_questao", "data_publicacao")

@admin.register(Alternativa)
class AlternativaAdmin(admin.ModelAdmin):
    list_display = ("questao", "texto_alternativa", "votos")
    # Filtros
    list_filter = ("questao",)