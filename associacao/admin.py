from django.contrib import admin
from .models import *


@admin.register(Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data')
    search_fields = ('titulo',)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data')


@admin.register(Esporte)
class EsporteAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_sugerido')


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'numero_socio',
        'cpf',
        'status_pagamento'
    )

    search_fields = ('nome', 'cpf')


@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('socio', 'ano')