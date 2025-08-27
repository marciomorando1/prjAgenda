from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'data_consulta', 'valor_consulta', 'situacao')
    list_filter = ('situacao', 'data_consulta')
    search_fields = ('paciente__nome',)
    ordering = ('-data_consulta',)