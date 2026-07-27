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


# =========================
# LOGIN
# =========================

# =========================
# DASHBOARD
# =========================
# =========================
# LOGOUT
# =========================

