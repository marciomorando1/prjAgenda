from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'telefone', 'cidade_natal', 'data_cadastro')
    search_fields = ('nome', 'email')
    ordering = ('-data_cadastro',)