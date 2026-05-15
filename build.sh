#!/bin/bash
set -e

uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
python manage.py collectstatic --noinput