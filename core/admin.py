from django.contrib import admin
from .models import Agendamento, Medico

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade', 'data', 'email', 'criado_em')
    list_filter = ('especialidade', 'data')
    search_fields = ('nome', 'email')

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especialidade', 'cidade', 'preco', 'nota', 'avaliacoes')
    prepopulated_fields = {'slug': ('nome',)}
    search_fields = ('nome', 'especialidade', 'cidade')
