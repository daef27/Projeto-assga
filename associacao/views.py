from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from datetime import datetime


# =========================
# HOME
# =========================

@staff_member_required
def adminpainel(request):
    return render(request, 'associacao/adminpainel.html')

def home(request):
    noticias = Noticia.objects.order_by('-data')[:3]
    return render(request, 'associacao/home.html', {'noticias': noticias})


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
    noticias = Noticia.objects.order_by('-data')
    return render(request, 'associacao/noticia.html', {'noticias': noticias})


def historia(request):
    historias = Historia.objects.order_by('-data')
    return render(request, 'associacao/historia.html', {'historias': historias})


def noticia_detalhe(request, noticia_id):
    noticia = get_object_or_404(Noticia, id=noticia_id)
    return render(request, 'associacao/noticia_detalhe.html', {'noticia': noticia})


# =========================
# LOGIN
# =========================

# =========================
# DASHBOARD / CARTEIRA
# =========================

def inscricao(request):
    message = None
    success = None
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        cpf = request.POST.get('cpf', '').strip()
        senha = request.POST.get('senha', '').strip()
        confirmar_senha = request.POST.get('confirmar_senha', '').strip()
        telefone = request.POST.get('telefone', '').strip()
        email = request.POST.get('email', '').strip()

        if not nome or not cpf or not senha or not confirmar_senha:
            message = 'Preencha todos os campos obrigatórios.'
        elif senha != confirmar_senha:
            message = 'As senhas não coincidem.'
        elif Socio.objects.filter(cpf=cpf).exists():
            message = 'CPF já registrado.'
        else:
            last = Socio.objects.order_by('-id').first()
            numero_socio = str(int(last.numero_socio) + 1) if last and last.numero_socio.isdigit() else '1001'
            Socio.objects.create(
                nome=nome,
                cpf=cpf,
                senha=senha,
                status_pagamento='Inativo',
                numero_socio=numero_socio,
            )
            success = 'Registro realizado com sucesso. Faça login para acessar sua identificação.'

    return render(request, 'associacao/inscricao.html', {'message': message, 'success': success})


def socio_login(request):
    message = None
    if request.method == 'POST':
        cpf = request.POST.get('cpf', '').strip()
        senha = request.POST.get('senha', '').strip()
        try:
            socio = Socio.objects.get(cpf=cpf, senha=senha)
            request.session['socio_id'] = socio.id
            return redirect('identificacao')
        except Socio.DoesNotExist:
            message = 'CPF ou senha incorretos.'
    return render(request, 'associacao/login.html', {'message': message})


def identificacao(request):
    socio_id = request.session.get('socio_id')
    if not socio_id:
        return redirect('login')

    try:
        socio = Socio.objects.get(id=socio_id)
    except Socio.DoesNotExist:
        return redirect('login')

    pagamentos = [
        (1, 'Janeiro', socio.pagamento_janeiro),
        (2, 'Fevereiro', socio.pagamento_fevereiro),
        (3, 'Março', socio.pagamento_marco),
        (4, 'Abril', socio.pagamento_abril),
        (5, 'Maio', socio.pagamento_maio),
        (6, 'Junho', socio.pagamento_junho),
        (7, 'Julho', socio.pagamento_julho),
        (8, 'Agosto', socio.pagamento_agosto),
        (9, 'Setembro', socio.pagamento_setembro),
        (10, 'Outubro', socio.pagamento_outubro),
        (11, 'Novembro', socio.pagamento_novembro),
        (12, 'Dezembro', socio.pagamento_dezembro),
    ]
    data_atual = datetime.now().strftime('%d/%m/%Y')
    ano_atual = datetime.now().year
    return render(request, 'associacao/dashboard.html', {
        'socio': socio,
        'pagamentos': pagamentos,
        'data_atual': data_atual,
        'ano_atual': ano_atual,
    })


def carteira(request):
    return redirect('identificacao')


def logout_view(request):
    request.session.pop('socio_id', None)
    return redirect('home')


# =========================
# =========================
# LOGOUT
# =========================

