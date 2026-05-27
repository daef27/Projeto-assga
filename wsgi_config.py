"""
Configuração WSGI para Vercel
"""
import os
import secrets
from pathlib import Path

# Gerar SECRET_KEY segura se não existir
if not os.environ.get("SECRET_KEY"):
    # Tentar ler de arquivo local (para dev)
    secret_file = Path(__file__).resolve().parent / ".secret_key"
    if secret_file.exists():
        with open(secret_file, "r") as f:
            os.environ["SECRET_KEY"] = f.read().strip()
    else:
        # Gerar chave aleatória para Vercel
        os.environ["SECRET_KEY"] = f"django-insecure-{secrets.token_urlsafe(50)}"

# Configurar DEBUG apenas se estiver explicitamente True
os.environ.setdefault("DEBUG", "False")

# Configurar DATABASE_URL para fallback
if not os.environ.get("DATABASE_URL"):
    os.environ["DATABASE_URL"] = "sqlite:///./db.sqlite3"

from core.wsgi import application
