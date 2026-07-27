from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('cursos/', views.cursos, name="cursos"),
    path('esportes/', views.esportes, name="esportes"),
    path('noticias/', views.noticias, name="noticias"),

    # Login, dashboard and adminpanel removed

]