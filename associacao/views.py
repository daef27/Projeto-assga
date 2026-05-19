from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def noticias(request):
    return render(request, "noticias.html")

def cursos(request):
    return render(request, "cursos.html")
