from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from .models import (
Noticia,
Curso,
Diretoria,
Esporte,
Evento,
Parceiro,
Historia
)


def algo(request):
    return render(request, 'associacao/algo.html')


@login_required
def dashboard(request):

    total_noticias = Noticia.objects.count()
    total_cursos = Curso.objects.count()
    total_eventos = Evento.objects.count()
    total_parceiros = Parceiro.objects.count()
    total_diretoria = Diretoria.objects.count()

    context = {
        'total_noticias': total_noticias,
        'total_cursos': total_cursos,
        'total_eventos': total_eventos,
        'total_parceiros': total_parceiros,
        'total_diretoria': total_diretoria,
    }

    return render(request, 'associacao/dashboard.html', context)


def home(request):
    noticias = Noticia.objects.all()[:3]
    cursos = Curso.objects.all()[:3]

    return render(request,'associacao/home.html',{
        'noticias': noticias,
        'cursos': cursos
    })


def noticia(request):
    noticias = Noticia.objects.all().order_by('-data')
    return render(request,'associacao/noticia.html',{
        'noticias': noticias
    })


def curso(request):
    cursos = Curso.objects.all()
    return render(request,'associacao/curso.html',{
        'cursos': cursos
    })


def diretoria(request):
    diretoria = Diretoria.objects.all()
    return render(request,'associacao/diretoria.html',{
        'diretoria': diretoria
    })


def esportes(request):
    esportes = Esporte.objects.all()
    return render(request,'associacao/esportes.html',{
        'esportes': esportes
    })


def evento(request):
    eventos = Evento.objects.all()
    return render(request,'associacao/evento.html',{
        'eventos': eventos
    })


def parceiros(request):
    parceiros = Parceiro.objects.all()
    return render(request,'associacao/parceiros.html',{
        'parceiros': parceiros
    })

def historia(request):
    historias = Historia.objects.all()
    return render(request, 'associacao/historia.html', {
        'historias': historias
    })

def inscricao(request):
    return render(request, 'associacao/inscricao.html')


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            return render(
                request,
                'associacao/login.html',
                {'erro': 'Usuário ou senha inválidos'}
            )

    return render(request, 'associacao/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')