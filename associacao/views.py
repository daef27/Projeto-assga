from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from .models import *
from datetime import datetime


# =========================
# HOME
# =========================

@staff_member_required
def adminpainel(request):
    return render(request, 'associacao/adminpainel.html')

def home(request):

    noticias = Noticia.objects.all().order_by('-data')[:5]
    parceiros = Parceiro.objects.all()

    return render(request, 'associacao/home.html', {
        'noticias': noticias,
        'parceiros': parceiros
    })


# =========================
# CURSOS
# =========================

def cursos(request):

    cursos = Curso.objects.all()
    parceiros = Parceiro.objects.all()

    return render(request, 'associacao/cursos.html', {
        'cursos': cursos,
        'parceiros': parceiros
    })


# =========================
# ESPORTES
# =========================

def esportes(request):

    esportes = Esporte.objects.all()
    clientes = Cliente.objects.all()
    doacoes = Doacao.objects.all()
    parceiros = Parceiro.objects.all()

    return render(request, 'associacao/esportes.html', {
        'esportes': esportes,
        'clientes': clientes,
        'doacoes': doacoes,
        'parceiros': parceiros
    })


# =========================
# NOTÍCIAS
# =========================

def noticias(request):

    noticias = Noticia.objects.all()
    parceiros = Parceiro.objects.all()

    return render(request, 'associacao/noticias.html', {
        'noticias': noticias,
        'parceiros': parceiros
    })


# =========================
# LOGIN
# =========================

def login_view(request):

    parceiros = Parceiro.objects.all()

    if request.method == "POST":

        cpf = request.POST.get('cpf')
        senha = request.POST.get('senha')

        try:
            socio = Socio.objects.get(cpf=cpf, senha=senha)

            request.session['socio_id'] = socio.id

            return redirect('dashboard')

        except:
            return render(request, 'associacao/login.html', {
                'erro': 'CPF ou senha inválidos',
                'parceiros': parceiros
            })

    return render(request, 'associacao/login.html', {
        'parceiros': parceiros
    })


# =========================
# DASHBOARD
# =========================

def dashboard(request):

    socio_id = request.session.get('socio_id')

    if not socio_id:
        return redirect('login')

    try:
        socio = Socio.objects.get(id=socio_id)
    except Socio.DoesNotExist:
        return redirect('login')

    historicos = Historico.objects.filter(socio=socio)

    pagamentos = {
        "Janeiro": True,
        "Fevereiro": False,
        "Março": True,
        "Abril": False,
        "Maio": True,
        "Junho": False,
        "Julho": False,
        "Agosto": False,
        "Setembro": False,
        "Outubro": False,
        "Novembro": False,
        "Dezembro": False
    }

    return render(request, 'associacao/dashboard.html', {

        'socio': socio,
        'historicos': historicos,
        'pagamentos': pagamentos,
        'data_atual': datetime.now().strftime("%d/%m/%Y"),
        'ano_atual': datetime.now().year

    })


# =========================
# LOGOUT
# =========================

def logout_view(request):

    request.session.flush()

    return redirect('login')