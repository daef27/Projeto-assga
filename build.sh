#!/bin/bash
set -e

uv pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput || echo "Migrate failed, continuing..."
python create_superuser.py || echo "Create superuser failed, continuing..."