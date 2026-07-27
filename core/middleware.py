import base64
from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


def _unauthorized():
    res = HttpResponse('Unauthorized', status=401)
    res['WWW-Authenticate'] = 'Basic realm="Restricted"'
    return res


class BasicAuthMiddleware(MiddlewareMixin):
    """Simple Basic HTTP auth middleware controlled by env vars.

    - ENABLE_BASIC_AUTH (True/False)
    - BASIC_AUTH_USER
    - BASIC_AUTH_PASSWORD

    Protects only admin URLs and logs in a Django admin user automatically.
    """

    def process_request(self, request):
        if not getattr(settings, 'ENABLE_BASIC_AUTH', False):
            return None

        # Only protect admin URLs. Keep public site and assets accessible.
        # Admin may be mounted at '/admin' (covers '/admin' and '/admin/...').
        if not request.path.startswith('/admin'):
            return None

        # allow static/media files (in case static is served under /admin/...)
        static_url = getattr(settings, 'STATIC_URL', '/static/')
        media_url = getattr(settings, 'MEDIA_URL', '/media/')
        if request.path.startswith(static_url) or request.path.startswith(media_url):
            return None

        auth = request.META.get('HTTP_AUTHORIZATION')
        if not auth:
            return _unauthorized()

        if not auth.startswith('Basic '):
            return _unauthorized()

        try:
            b64 = auth.split(' ', 1)[1]
            decoded = base64.b64decode(b64).decode('utf-8')
        except Exception:
            return _unauthorized()

        if ':' not in decoded:
            return _unauthorized()

        user, passwd = decoded.split(':', 1)
        if user != getattr(settings, 'BASIC_AUTH_USER', '') or passwd != getattr(settings, 'BASIC_AUTH_PASSWORD', ''):
            return _unauthorized()

        if hasattr(request, 'user') and request.user.is_authenticated:
            return None

        UserModel = get_user_model()
        try:
            django_user = UserModel.objects.get(username=user)
        except UserModel.DoesNotExist:
            django_user = UserModel.objects.create(
                username=user,
                is_staff=True,
                is_superuser=True,
                is_active=True,
            )
            django_user.set_unusable_password()
            django_user.save()
        else:
            changed = False
            if not django_user.is_staff:
                django_user.is_staff = True
                changed = True
            if not django_user.is_active:
                django_user.is_active = True
                changed = True
            if changed:
                django_user.save()

        login(request, django_user)
        return None
