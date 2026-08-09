from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from associacao import views

urlpatterns = [
    # Redireciona /admin/login/ para a tela de login customizada
    re_path(r'^admin/login/$', views.redirect_admin_login, name='admin_login_redirect'),

    # Admin (protected via Basic Auth middleware)
    path('admin/', admin.site.urls),

    # APP ASSOCIACAO
    path('', include('associacao.urls')),
]

# MEDIA
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

# STATIC
urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)