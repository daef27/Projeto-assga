#!/bin/bash
set -e

echo "🚀 Iniciando build (build_files.sh)..."

# Garante o diretório public
mkdir -p public

# Migrações
echo "📦 Aplicando migrações..."
python3 manage.py migrate --noinput

# Coleta estáticos
echo "🎨 Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput

echo "✅ Build concluído!"
