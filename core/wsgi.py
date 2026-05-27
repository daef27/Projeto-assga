import os
import sys
import secrets
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Configuração inicial para Vercel
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Configurar SECRET_KEY
if not os.environ.get("SECRET_KEY"):
    os.environ["SECRET_KEY"] = f"django-insecure-{secrets.token_urlsafe(50)}"

# Configurar DEBUG
os.environ.setdefault("DEBUG", "False")

# Configurar DATABASE_URL
if not os.environ.get("DATABASE_URL"):
    os.environ["DATABASE_URL"] = f"sqlite:///{BASE_DIR}/db.sqlite3"

# Configurar DJANGO_SETTINGS_MODULE
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Configurar Varelas Vercel
if os.environ.get('VERCEL'):
    os.environ['ALLOWED_HOSTS'] = '*'

application = get_wsgi_application()