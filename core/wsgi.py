import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Configuração inicial para Vercel
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Importar configurações de WSGI (SECRET_KEY, DATABASE_URL, etc)
try:
    import wsgi_config
except ImportError:
    pass

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()