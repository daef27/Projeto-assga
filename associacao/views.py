from django.shortcuts import render
from .models import Socio
from django.db import connection


def home(request):
    try:
        socios = Socio.objects.all()
    except:
        with connection.schema_editor() as schema:
            schema.create_model(Socio)
        socios = Socio.objects.all()

    return render(request, 'associacao/home.html', {'socios': socios})