from django.urls import path
from . import views

urlpatterns = [
    path('algo/', views.algo, name='algo'),
    path('', views.home, name='home'),
    path('esportes/', views.esportes, name='esportes'),
    path('curso/', views.curso, name='curso'),
    path('evento/', views.evento, name='evento'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('parceiros/', views.parceiros, name='parceiros'),
    path('historia/', views.historia, name='historia'),
    path('diretoria/', views.diretoria, name='diretoria'),
    path('noticia/', views.noticia, name='noticia'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inscricao/', views.inscricao, name='inscricao'),
]