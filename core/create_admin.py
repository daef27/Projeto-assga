from django.contrib.auth import get_user_model
import os

User = get_user_model()

username = os.getenv("ADMIN_USER")
password = os.getenv("ADMIN_PASSWORD")
email = os.getenv("ADMIN_EMAIL")

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )