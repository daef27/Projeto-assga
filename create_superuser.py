import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')

if not username or not password:
    print('Variáveis de ambiente DJANGO_SUPERUSER_USERNAME e DJANGO_SUPERUSER_PASSWORD não definidas. Pulando criação de superusuário.')
else:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, password=password, email=email or 'admin@example.com')
        print(f'Superusuário "{username}" criado com sucesso!')
    else:
        print(f'Superusuário "{username}" já existe.')
