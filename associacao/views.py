from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import *
from datetime import datetime


# =========================
# DASHBOARD / CARTEIRA
# =========================

def carteira(request):
    socios = Socio.objects.all()
    socio = socios.first() if socios.exists() else None
    pagamentos = {
        'Janeiro': True,
        'Fevereiro': False,
        'Março': True,
        'Abril': True,
        'Maio': False,
        'Junho': True,
        'Julho': True,
        'Agosto': False,
        'Setembro': True,
        'Outubro': True,
        'Novembro': False,
        'Dezembro': True,
    }
    historicos = Historico.objects.filter(socio=socio) if socio else []
    return render(request, 'associacao/dashboard.html', {
        'socios': socios,
        'socio': socio,
        'pagamentos': pagamentos,
        'historicos': historicos,
        'data_atual': datetime.now().strftime('%d/%m/%Y'),
        'ano_atual': datetime.now().year,
    })


def logout_view(request):
    return redirect('home')


# =========================
# HOME
# =========================

@staff_member_required
def adminpainel(request):
    return render(request, 'associacao/adminpainel.html')

def home(request):
    return render(request, 'associacao/home.html')


# =========================
# CURSOS
# =========================


def cursos(request):
    return render(request, 'associacao/esportes.html')


# =========================
# ESPORTES
# =========================


def esportes(request):
    return render(request, 'associacao/esportes.html')


# =========================
# NOTÍCIAS
# =========================


def noticias(request):
    return render(request, 'associacao/noticia.html')
