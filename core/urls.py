from django.contrib import admin
from django.urls import path
from associacao import views

urlpatterns = [
    path("admin/", admin.site.urls),

    path("", views.home, name="home"),
    path("noticias/", views.noticias, name="noticias"),
    path("cursos/", views.cursos, name="cursos"),
]