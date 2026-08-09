from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.utils.deprecation import MiddlewareMixin


class AutoLoginAdminMiddleware(MiddlewareMixin):
    """Auto-autentica um usuário admin específico para que /admin/ abra
    diretamente, sem tela de login.

    Credenciais configuradas via env vars (com fallback para dev):
    - ADMIN_AUTO_USER (default: 'admin')
    - ADMIN_AUTO_PASSWORD (default: 'admin123')
    """

    def process_request(self, request):
        # Só interfere em URLs do admin.
        if not request.path.startswith('/admin'):
            return None

        UserModel = get_user_model()

        username = getattr(settings, 'ADMIN_AUTO_USER', 'admin')
        password = getattr(settings, 'ADMIN_AUTO_PASSWORD', 'admin123')

        # Já autenticado? Nada a fazer.
        if getattr(request, 'user', None) is not None and request.user.is_authenticated:
            return None

        # Procura ou cria o usuário admin.
        user, created = UserModel.objects.get_or_create(
            username=username,
            defaults={
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
            },
        )
        if created:
            user.set_password(password)
        else:
            changed = False
            if not user.is_staff:
                user.is_staff = True
                changed = True
            if not user.is_superuser:
                user.is_superuser = True
                changed = True
            if not user.is_active:
                user.is_active = True
                changed = True
            if changed:
                user.save()

        # Autentica (login silencioso) para abrir o admin direto.
        login(request, user)
        return None


class AccessLogMiddleware(MiddlewareMixin):
    """Log accesses to the identificacao page for admin review."""

    def process_request(self, request):
        if request.path != '/identificacao/':
            return None

        try:
            from associacao.models import IdentificacaoLog
            remote_addr = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
            IdentificacaoLog.objects.create(
                path=request.path,
                method=request.method,
                remote_addr=remote_addr,
                user_agent=request.META.get('HTTP_USER_AGENT', ''),
            )
        except Exception:
            pass

        return None
