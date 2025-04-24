from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'endereco', 'telefone', 'genero', 'estado_civil', 'data_cadastro')
    search_fields = ('nome', 'cpf')
    list_filter = ('nome', 'sobrenome')
    ordering = ('nome',)
