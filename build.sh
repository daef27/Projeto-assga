#!/bin/bash
set -e

uv pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate --noinput