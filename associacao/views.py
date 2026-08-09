from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from datetime import datetime


# =========================
# LOGIN ADMIN CUSTOMIZADO
# =========================

def redirect_admin_login(request):
    """Redireciona /admin/login/ para a tela de login customizada, preservando o 'next'."""
    next_url = request.GET.get('next', '')
    if next_url:
        return redirect(f"{reverse('admin_login')}?next={next_url}")
    return redirect('admin_login')


def admin_login(request):
    """Página de login customizada para o painel administrativo."""
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('adminpainel')

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:
                login(request, user)
                next_url = request.POST.get('next', request.GET.get('next', 'adminpainel'))
                return redirect(next_url if next_url.startswith('/') else 'adminpainel')
            else:
                messages.error(request, 'Este usuário não tem permissão de acesso ao painel.')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    # ---------- CONTAGENS E LISTAGENS (overview) ----------
    def _count(model):
        def f():
            return model.objects.count()
        return safe_query(f, 0)

    contagens = {
        'socios': _count(Socio),
        'noticias': _count(Noticia),
        'eventos': _count(Evento),
        'parceiros': _count(Parceiro),
        'historias': _count(Historia),
        'cursos': _count(Curso),
        'esportes': _count(Esporte),
        'diretoria': _count(Diretoria),
        'clientes': _count(Cliente),
        'doacoes': _count(Doacao),
        'historicos': _count(Historico),
        'logs': _count(IdentificacaoLog),
    }

    socios = safe_all(Socio.objects.order_by('-id')[:8])
    noticias = safe_all(Noticia.objects.order_by('-id')[:8])
    eventos = safe_all(Evento.objects.order_by('-id')[:8])
    parceiros = safe_all(Parceiro.objects.all()[:8])
    historias = safe_all(Historia.objects.order_by('-id')[:8])
    cursos = safe_all(Curso.objects.order_by('-id')[:8])
    esportes = safe_all(Esporte.objects.all()[:8])
    diretoria = safe_all(Diretoria.objects.all()[:8])
    clientes = safe_all(Cliente.objects.all()[:8])
    doacoes = safe_all(Doacao.objects.all()[:8])
    historicos = safe_all(Historico.objects.order_by('-id')[:8])
    logs = safe_all(IdentificacaoLog.objects.order_by('-id')[:8])

    return render(request, 'associacao/admin_login.html', {
        'contagens': contagens,
        'socios': socios,
        'noticias': noticias,
        'eventos': eventos,
        'parceiros': parceiros,
        'historias': historias,
        'cursos': cursos,
        'esportes': esportes,
        'diretoria': diretoria,
        'clientes': clientes,
        'doacoes': doacoes,
        'historicos': historicos,
        'logs': logs,
    })


def admin_logout(request):
    """Desloga o usuário do painel administrativo."""
    logout(request)
    return redirect('admin_login')


# =========================
# HELPERS (CONSULTAS SEGURAS)
# =========================

def safe_query(fn, default=None):
    """Executa uma consulta ao banco com segurança.
    Se o banco estiver indisponível ou a consulta falhar,
    retorna o valor padrão (default) em vez de gerar 500."""
    try:
        return fn()
    except Exception:
        return default


def safe_all(queryset):
    """Retorna a lista de objetos, ou [] se o banco estiver indisponível."""
    return safe_query(lambda: list(queryset), [])


def get_parceiros():
    """Retorna os parceiros para o footer, ou [] se indisponível."""
    return safe_all(Parceiro.objects.all())


# =========================
# HOME
# =========================

@staff_member_required
def adminpainel(request):
    """Página de cadastro rápido no admin para Sócio, Notícia e Evento."""
    mensagens = []
    erros = []

    if request.method == 'POST':
        tipo = request.POST.get('tipo')

        # ---------- CADASTRO DE SÓCIO ----------
        if tipo == 'socio':
            nome = request.POST.get('nome', '').strip()
            cpf = request.POST.get('cpf', '').strip()
            senha = request.POST.get('senha', '').strip()
            numero_socio = request.POST.get('numero_socio', '').strip()
            investimento = request.POST.get('investimento', '').strip()

            if not nome or not cpf:
                erros.append('Preencha nome e CPF do sócio.')
            elif safe_query(lambda: Socio.objects.filter(cpf=cpf).exists(), False):
                erros.append('Já existe um sócio com este CPF.')
            else:
                def _salvar_socio():
                    if not numero_socio:
                        last = Socio.objects.order_by('-id').first()
                        numero = int(last.numero_socio) + 1 if last and last.numero_socio.isdigit() else 1001
                    else:
                        numero = numero_socio
                    Socio.objects.create(
                        nome=nome,
                        cpf=cpf,
                        senha=senha or '123456',
                        numero_socio=str(numero),
                        investimento=investimento or 0,
                    )
                    return True
                if safe_query(_salvar_socio, False):
                    mensagens.append(f'Sócio "{nome}" cadastrado com sucesso!')
                else:
                    erros.append('Não foi possível cadastrar o sócio. Tente novamente.')

        # ---------- CADASTRO DE NOTÍCIA ----------
        elif tipo == 'noticia':
            titulo = request.POST.get('titulo', '').strip()
            texto = request.POST.get('texto', '').strip()
            imagem = request.FILES.get('imagem')

            if not titulo or not texto:
                erros.append('Preencha título e texto da notícia.')
            else:
                def _salvar_noticia():
                    Noticia.objects.create(titulo=titulo, texto=texto, imagem=imagem)
                    return True
                if safe_query(_salvar_noticia, False):
                    mensagens.append(f'Notícia "{titulo}" cadastrada com sucesso!')
                else:
                    erros.append('Não foi possível cadastrar a notícia.')

        # ---------- CADASTRO DE EVENTO ----------
        elif tipo == 'evento':
            titulo = request.POST.get('titulo', '').strip()
            descricao = request.POST.get('descricao', '').strip()
            data = request.POST.get('data', '').strip()
            imagem = request.FILES.get('imagem')

            if not titulo or not descricao or not data:
                erros.append('Preencha título, descrição e data do evento.')
            else:
                def _salvar_evento():
                    Evento.objects.create(titulo=titulo, descricao=descricao, data=data, imagem=imagem)
                    return True
                if safe_query(_salvar_evento, False):
                    mensagens.append(f'Evento "{titulo}" cadastrado com sucesso!')
                else:
                    erros.append('Não foi possível cadastrar o evento.')

# ---------- LISTAGENS RECENTES (limitadas) ----------
    socios = safe_all(Socio.objects.order_by('-id')[:8])
    noticias = safe_all(Noticia.objects.order_by('-id')[:8])
    eventos = safe_all(Evento.objects.order_by('-id')[:8])
    parceiros = safe_all(Parceiro.objects.all()[:8])
    historias = safe_all(Historia.objects.order_by('-id')[:8])
    cursos = safe_all(Curso.objects.order_by('-id')[:8])
    esportes = safe_all(Esporte.objects.all()[:8])
    diretoria = safe_all(Diretoria.objects.all()[:8])
    clientes = safe_all(Cliente.objects.all()[:8])
    doacoes = safe_all(Doacao.objects.all()[:8])
    historicos = safe_all(Historico.objects.order_by('-id')[:8])
    logs = safe_all(IdentificacaoLog.objects.order_by('-id')[:8])

    # ---------- CONTAGENS (overview) ----------
    def _count(model):
        def f():
            return model.objects.count()
        return safe_query(f, 0)

    contagens = {
        'socios': _count(Socio),
        'noticias': _count(Noticia),
        'eventos': _count(Evento),
        'parceiros': _count(Parceiro),
        'historias': _count(Historia),
        'cursos': _count(Curso),
        'esportes': _count(Esporte),
        'diretoria': _count(Diretoria),
        'clientes': _count(Cliente),
        'doacoes': _count(Doacao),
        'historicos': _count(Historico),
        'logs': _count(IdentificacaoLog),
    }

    return render(request, 'associacao/adminpainel.html', {
        'mensagens': mensagens,
        'erros': erros,
        'socios': socios,
        'noticias': noticias,
        'eventos': eventos,
        'parceiros': parceiros,
        'historias': historias,
        'cursos': cursos,
        'esportes': esportes,
        'diretoria': diretoria,
        'clientes': clientes,
        'doacoes': doacoes,
        'historicos': historicos,
        'logs': logs,
        'contagens': contagens,
    })

def home(request):
    noticias = safe_all(Noticia.objects.order_by('-data')[:3])
    return render(request, 'associacao/home.html', {
        'noticias': noticias,
        'parceiros': get_parceiros(),
    })


# =========================
# CURSOS
# =========================

def cursos(request):
    cursos = safe_all(Curso.objects.all())
    return render(request, 'associacao/curso.html', {
        'cursos': cursos,
        'parceiros': get_parceiros(),
    })


# =========================
# ESPORTES
# =========================

def esportes(request):
    esportes = safe_all(Esporte.objects.all())
    clientes = safe_all(Cliente.objects.all())
    doacoes = safe_all(Doacao.objects.all())
    return render(request, 'associacao/esportes.html', {
        'esportes': esportes,
        'clientes': clientes,
        'doacoes': doacoes,
        'parceiros': get_parceiros(),
    })


# =========================
# DIRETORIA
# =========================

def diretoria(request):
    diretoria = safe_all(Diretoria.objects.all())
    return render(request, 'associacao/diretoria.html', {
        'diretoria': diretoria,
        'parceiros': get_parceiros(),
    })


# =========================
# EVENTOS
# =========================

def eventos(request):
    eventos = safe_all(Evento.objects.order_by('-data'))
    return render(request, 'associacao/evento.html', {
        'eventos': eventos,
        'parceiros': get_parceiros(),
    })


# =========================
# NOTÍCIAS
# =========================

def noticias(request):
    noticias = safe_all(Noticia.objects.order_by('-data'))
    return render(request, 'associacao/noticia.html', {
        'noticias': noticias,
        'parceiros': get_parceiros(),
    })


def historia(request):
    historias = safe_all(Historia.objects.order_by('-data'))
    return render(request, 'associacao/historia.html', {
        'historias': historias,
        'parceiros': get_parceiros(),
    })


def noticia_detalhe(request, noticia_id):
    noticia = safe_query(
        lambda: get_object_or_404(Noticia, id=noticia_id),
        None
    )
    if noticia is None:
        return render(request, 'associacao/noticia.html', {
            'noticias': [],
            'parceiros': get_parceiros(),
        })
    return render(request, 'associacao/noticia_detalhe.html', {
        'noticia': noticia,
        'parceiros': get_parceiros(),
    })


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
        else:
            cpf_existe = safe_query(lambda: Socio.objects.filter(cpf=cpf).exists(), False)
            if cpf_existe:
                message = 'CPF já registrado.'
            else:
                def _registrar():
                    last = Socio.objects.order_by('-id').first()
                    numero_socio = str(int(last.numero_socio) + 1) if last and last.numero_socio.isdigit() else '1001'
                    Socio.objects.create(
                        nome=nome,
                        cpf=cpf,
                        senha=senha,
                        status_pagamento='Inativo',
                        numero_socio=numero_socio,
                    )
                    return True
                if safe_query(_registrar, False):
                    success = 'Registro realizado com sucesso. Faça login para acessar sua identificação.'
                else:
                    message = 'Não foi possível completar o registro agora. Tente novamente mais tarde.'

    return render(request, 'associacao/inscricao.html', {
        'message': message,
        'success': success,
        'parceiros': get_parceiros(),
    })


def socio_login(request):
    message = None
    if request.method == 'POST':
        cpf = request.POST.get('cpf', '').strip()
        senha = request.POST.get('senha', '').strip()
        socio = safe_query(lambda: Socio.objects.get(cpf=cpf, senha=senha), None)
        if socio is not None:
            request.session['socio_id'] = socio.id
            return redirect('identificacao')
        else:
            message = 'CPF ou senha incorretos.'
    return render(request, 'associacao/login.html', {
        'message': message,
        'parceiros': get_parceiros(),
    })


def identificacao(request):
    socio_id = request.session.get('socio_id')
    if not socio_id:
        return redirect('login')

    socio = safe_query(lambda: Socio.objects.get(id=socio_id), None)
    if socio is None:
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
        'parceiros': get_parceiros(),
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

