from django.utils.deprecation import MiddlewareMixin


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
