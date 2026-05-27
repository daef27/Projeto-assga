#!/usr/bin/env python
"""
Script para preparar o Django para Vercel
"""
import os
import sys
import secrets
import django
from pathlib import Path

# Definir variáveis de ambiente
if not os.environ.get("SECRET_KEY"):
    os.environ["SECRET_KEY"] = f"django-insecure-{secrets.token_urlsafe(50)}"

if not os.environ.get("DEBUG"):
    os.environ["DEBUG"] = "False"

if not os.environ.get("DATABASE_URL"):
    os.environ["DATABASE_URL"] = "sqlite:///./db.sqlite3"

# Configurar Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

# Importar modelos
from django.core.management import call_command
from django.contrib.auth.models import User

def setup_vercel():
    """Configurar ambiente Vercel"""
    print("🔧 Preparando ambiente Vercel...")
    
    try:
        # Criar superusuário padrão se não existir
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123"
            )
            print("✓ Superusuário 'admin' criado")
        else:
            print("✓ Superusuário 'admin' já existe")
    except Exception as e:
        print(f"⚠ Erro ao criar superusuário: {e}")

if __name__ == "__main__":
    setup_vercel()
    print("✓ Preparação concluída!")
