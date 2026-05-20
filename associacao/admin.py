from django.contrib import admin
from .models import Parceiro, Noticia, Curso, Esporte, Cliente, Doacao, Socio, Historico

try:
    @admin.register(Parceiro)
    class ParceiroAdmin(admin.ModelAdmin):
        list_display = ('nome',)
except:
    pass

try:
    @admin.register(Noticia)
    class NoticiaAdmin(admin.ModelAdmin):
        list_display = ("titulo",)
except:
    pass

try:
    @admin.register(Curso)
    class CursoAdmin(admin.ModelAdmin):
        list_display = ('titulo', 'data')
except:
    pass

try:
    @admin.register(Esporte)
    class EsporteAdmin(admin.ModelAdmin):
        list_display = ('nome',)
except:
    pass

try:
    @admin.register(Cliente)
    class ClienteAdmin(admin.ModelAdmin):
        list_display = ('nome',)
except:
    pass

try:
    @admin.register(Doacao)
    class DoacaoAdmin(admin.ModelAdmin):
        list_display = ('nome', 'valor_sugerido')
except:
    pass

try:
    @admin.register(Socio)
    class SocioAdmin(admin.ModelAdmin):
        list_display = (
            'nome',
            'numero_socio',
            'cpf',
            'status_pagamento'
        )
        search_fields = ('nome', 'cpf')
except:
    pass

try:
    @admin.register(Historico)
    class HistoricoAdmin(admin.ModelAdmin):
        list_display = ('socio', 'ano')
except:
    pass
