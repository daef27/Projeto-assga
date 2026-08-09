#!/bin/bash
set -e

echo "🚀 Iniciando build do ASSGA..."

# Cria diretório public (compatibilidade com Vercel)
mkdir -p public

# Roda as migrações do banco de dados
echo "📦 Aplicando migrações..."
python manage.py migrate --noinput

# Cria superusuário se as variáveis de ambiente estiverem definidas
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    echo "👤 Criando superusuário..."
    python create_superuser.py || echo "⚠️  Aviso: falha ao criar superusuário (pode já existir)."
fi

# Coleta arquivos estáticos
echo "🎨 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "✅ Build concluído com sucesso!"
