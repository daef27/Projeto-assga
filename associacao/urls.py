from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('cursos/', views.cursos, name="cursos"),
    path('esportes/', views.esportes, name="esportes"),
    path('diretoria/', views.diretoria, name="diretoria"),
    path('eventos/', views.eventos, name="eventos"),
    path('noticias/', views.noticias, name="noticias"),
    path('noticias/<int:noticia_id>/', views.noticia_detalhe, name="noticia_detalhe"),
    path('historia/', views.historia, name="historia"),
    path('inscricao/', views.inscricao, name="inscricao"),
    path('login/', views.socio_login, name="login"),
    path('carteira/', views.carteira, name="carteira"),
    path('identificacao/', views.identificacao, name="identificacao"),
    path('logout/', views.logout_view, name="logout"),
    path('adminpainel/', views.adminpainel, name="adminpainel"),
]
