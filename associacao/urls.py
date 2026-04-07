from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="home"),
    path('cursos/', views.cursos, name="cursos"),
    path('esportes/', views.esportes, name="esportes"),
    path('noticias/', views.noticias, name="noticias"),

    path('login/', views.login_view, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout_view, name="logout"),
    path('adminpainel/', views.adminpainel, name='adminpainel'),

]