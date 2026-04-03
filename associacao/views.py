from django.shortcuts import render
from .models import Socio

def home(request):
    socios = Socio.objects.all()
    return render(request, 'home.html', {'socios': socios})