from django.contrib import admin
from .models import Parceiro, Noticia, Curso, Esporte, Cliente, Doacao, Socio, Historico


# Customizar títulos do admin
admin.site.site_header = "📊 Painel de Administração ASSGA"
admin.site.site_title = "ASSGA Admin"
admin.site.index_title = "Bem-vindo ao Painel de Dados"


# =========================
# PARCEIROS
# =========================
@admin.register(Parceiro)
class ParceiroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tem_logo')
    search_fields = ('nome',)
    ordering = ('nome',)
    
    def tem_logo(self, obj):
        return '✅ Sim' if obj.logo else '❌ Não'
    tem_logo.short_description = 'Tem Logo'


# =========================
# NOTÍCIAS
# =========================
@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'tem_imagem')
    search_fields = ('titulo', 'texto')
    list_filter = ('data',)
    ordering = ('-data',)
    date_hierarchy = 'data'
    
    def tem_imagem(self, obj):
        return '✅ Sim' if obj.imagem else '❌ Não'
    tem_imagem.short_description = 'Tem Imagem'


# =========================
# CURSOS
# =========================
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'tem_imagem')
    search_fields = ('titulo', 'descricao')
    list_filter = ('data',)
    ordering = ('-data',)
    date_hierarchy = 'data'
    
    def tem_imagem(self, obj):
        return '✅ Sim' if obj.imagem else '❌ Não'
    tem_imagem.short_description = 'Tem Imagem'


# =========================
# ESPORTES
# =========================
@admin.register(Esporte)
class EsporteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tem_imagem')
    search_fields = ('nome', 'descricao')
    ordering = ('nome',)
    
    def tem_imagem(self, obj):
        return '✅ Sim' if obj.imagem else '❌ Não'
    tem_imagem.short_description = 'Tem Imagem'


# =========================
# CLIENTES
# =========================
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site_link', 'tem_logo')
    search_fields = ('nome', 'site')
    ordering = ('nome',)
    
    def site_link(self, obj):
        if obj.site:
            return f'<a href="{obj.site}" target="_blank">🔗 Visitar</a>'
        return '❌ Sem site'
    site_link.allow_tags = True
    site_link.short_description = 'Site'
    
    def tem_logo(self, obj):
        return '✅ Sim' if obj.logo else '❌ Não'
    tem_logo.short_description = 'Tem Logo'


# =========================
# DOAÇÕES
# =========================
@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_sugerido', 'tem_qrcode')
    search_fields = ('nome',)
    ordering = ('nome',)
    
    def tem_qrcode(self, obj):
        return '✅ Sim' if obj.qr_code else '❌ Não'
    tem_qrcode.short_description = 'Tem QR Code'


# =========================
# SÓCIOS
# =========================
@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('numero_socio', 'nome', 'status_pagamento', 'investimento', 'tem_foto')
    list_filter = ('status_pagamento',)
    search_fields = ('nome', 'numero_socio', 'cpf')
    readonly_fields = ('cpf', 'numero_socio')
    ordering = ('numero_socio',)
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'cpf', 'numero_socio', 'foto')
        }),
        ('Status e Investimento', {
            'fields': ('status_pagamento', 'investimento')
        }),
    )

    # O campo senha não é usado para login público do site, então não expomos no admin.
    exclude = ('senha',)

    def tem_foto(self, obj):
        return '✅ Sim' if obj.foto else '❌ Não'
    tem_foto.short_description = 'Tem Foto'


# =========================
# HISTÓRICO
# =========================
@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('socio_nome', 'ano')
    list_filter = ('ano',)
    search_fields = ('socio__nome', 'ano')
    ordering = ('-ano', 'socio')
    
    def socio_nome(self, obj):
        return obj.socio.nome
    socio_nome.short_description = 'Sócio'
