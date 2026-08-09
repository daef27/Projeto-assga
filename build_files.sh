#!/bin/bash
set -e

echo "🚀 Iniciando build (build_files.sh)..."

# Garante o diretório public
mkdir -p public

# Migrações (não falha o build se o banco estiver indisponível)
echo "📦 Aplicando migrações..."
python3 manage.py migrate --noinput || echo "⚠️  Aviso: falha ao aplicar migrações (banco de dados indisponível). Continuando o build."

# Coleta estáticos
echo "🎨 Coletando arquivos estáticos..."
python3 manage.py collectstatic --noinput

echo "✅ Build concluído!"
