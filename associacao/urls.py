from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('cursos/', views.cursos, name="cursos"),
    path('esportes/', views.esportes, name="esportes"),
    path('noticias/', views.noticias, name="noticias"),
    path('carteira/', views.carteira, name="carteira"),
    path('identificacao/', views.carteira, name="identificacao"),
    path('logout/', views.logout_view, name="logout"),

    # Login, dashboard and adminpanel removed

]