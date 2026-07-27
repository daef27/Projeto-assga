import base64
from django.conf import settings
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

    Leaves static and media URLs accessible without auth.
    """

    def process_request(self, request):
        if not getattr(settings, 'ENABLE_BASIC_AUTH', False):
            return None

        # allow static/media files
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
        if user == getattr(settings, 'BASIC_AUTH_USER', '') and passwd == getattr(settings, 'BASIC_AUTH_PASSWORD', ''):
            return None

        return _unauthorized()
