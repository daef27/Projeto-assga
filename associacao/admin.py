from django.contrib import admin
from .models import Parceiro, Noticia, Historia, Curso, Esporte, Diretoria, Evento, Cliente, Doacao, Socio, Historico, IdentificacaoLog


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
    list_display = ('titulo', 'data', 'valor', 'tem_imagem')
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
# DIRETORIA
# =========================
@admin.register(Diretoria)
class DiretoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'tem_foto')
    search_fields = ('nome', 'cargo')
    ordering = ('nome',)
    
    def tem_foto(self, obj):
        return '✅ Sim' if obj.foto else '❌ Não'
    tem_foto.short_description = 'Tem Foto'


# =========================
# EVENTOS
# =========================
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'tem_imagem')
    search_fields = ('titulo', 'descricao')
    list_filter = ('data',)
    ordering = ('-data',)
    date_hierarchy = 'data'
    
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
# HISTÓRIA

@admin.register(Historia)
class HistoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data', 'tem_imagem')
    search_fields = ('titulo', 'texto')
    list_filter = ('data',)
    ordering = ('-data',)

    def tem_imagem(self, obj):
        return '✅ Sim' if obj.imagem else '❌ Não'
    tem_imagem.short_description = 'Tem Imagem'


# =========================
# SÓCIOS
# =========================
@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('numero_socio', 'nome', 'cpf', 'status_pagamento', 'investimento', 'tem_foto')
    list_filter = ('status_pagamento',)
    search_fields = ('nome', 'numero_socio', 'cpf')
    ordering = ('numero_socio',)
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'cpf', 'senha', 'numero_socio', 'foto')
        }),
        ('Status e Investimento', {
            'fields': ('status_pagamento', 'investimento')
        }),
        ('Mensalidades (Janeiro a Dezembro)', {
            'fields': (
                'pagamento_janeiro',
                'pagamento_fevereiro',
                'pagamento_marco',
                'pagamento_abril',
                'pagamento_maio',
                'pagamento_junho',
                'pagamento_julho',
                'pagamento_agosto',
                'pagamento_setembro',
                'pagamento_outubro',
                'pagamento_novembro',
                'pagamento_dezembro',
            )
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.numero_socio:
            last = Socio.objects.order_by('-id').first()
            obj.numero_socio = str(int(last.numero_socio) + 1) if last and last.numero_socio.isdigit() else '1001'
        super().save_model(request, obj, form, change)

    def tem_foto(self, obj):
        return '✅ Sim' if obj.foto else '❌ Não'
    tem_foto.short_description = 'Tem Foto'


# =========================
# HISTÓRICO
# =========================
@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('ano', 'data', 'tem_imagem')
    list_filter = ('ano', 'data')
    search_fields = ('socio__nome', 'ano', 'texto')
    ordering = ('-data', 'socio')
    fields = ('socio', 'ano', 'data', 'texto', 'imagem')
    readonly_fields = ()

    def tem_imagem(self, obj):
        return '✅ Sim' if obj.imagem else '❌ Não'
    tem_imagem.short_description = 'Tem Imagem'


@admin.register(IdentificacaoLog)
class IdentificacaoLogAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'remote_addr', 'timestamp')
    list_filter = ('method', 'path', 'timestamp')
    search_fields = ('path', 'remote_addr', 'user_agent')
    readonly_fields = ('path', 'method', 'remote_addr', 'user_agent', 'timestamp')
    ordering = ('-timestamp',)
