import os
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured

try:
    import dj_database_url
except ImportError:
    dj_database_url = None



BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "django-secret")



DEBUG = True



ALLOWED_HOSTS = ["*"]



CSRF_TRUSTED_ORIGINS = [

    "http://127.0.0.1:8000",

    "http://localhost:8000",

    "https://projeto-alpha-weld.vercel.app",

    "https://*.vercel.app",

]



INSTALLED_APPS = [

    "django.contrib.admin",

    "django.contrib.auth",

    "django.contrib.contenttypes",

    "django.contrib.sessions",

    "django.contrib.messages",

    "django.contrib.staticfiles",



    "associacao",

]



MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]



ROOT_URLCONF = "core.urls"



TEMPLATES = [

    {

        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [BASE_DIR / "templates"],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.debug",

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",

            ],

        },

    },

]



WSGI_APPLICATION = "core.wsgi.application"



DATABASE_URL = os.environ.get("DATABASE_URL", "").strip()

if DATABASE_URL and dj_database_url:
    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=True)
    }
else:
    raise ImproperlyConfigured("DATABASE_URL environment variable not set or dj_database_url not available")

LANGUAGE_CODE = "pt-br"



TIME_ZONE = "America/Sao_Paulo"



USE_I18N = True

USE_TZ = True



STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"



MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"



DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



STATICFILES_STORAGE = (

    "whitenoise.storage.CompressedManifestStaticFilesStorage"

)



LOGIN_REDIRECT_URL = "/admin/"

LOGIN_URL = "/admin/login/"