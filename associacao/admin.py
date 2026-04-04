from django.contrib import admin
from .models import (
    Noticia,
    Curso,
    Diretoria,
    Esporte,
    Evento,
    Parceiro,
    Historia,
    Membro
)

admin.site.register(Noticia)
admin.site.register(Curso)
admin.site.register(Diretoria)
admin.site.register(Esporte)
admin.site.register(Evento)
admin.site.register(Parceiro)
admin.site.register(Historia)
admin.site.register(Membro)