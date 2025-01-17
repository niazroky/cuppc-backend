from datetime import timedelta
from pathlib import Path
from os import getenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xmr^gkzos*ih@23wmo&@%%#tfek854yx3kcmflxdtk6c!22cx7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = getenv("IS_DEBUG", "True")

ALLOWED_HOSTS = [
    getenv("APP_HOST")
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Custom Apps for the Django project.
    # - 'rest_framework': Enables Django REST framework to build APIs.
    # - 'rest_framework_simplejwt': Adds support for JWT authentication using the Simple JWT package.
    # - 'users': Custom app for managing user-related models and views (e.g., Student, Teacher).
    'rest_framework',
    'rest_framework_simplejwt',
    'users',
    'corsheaders',
]


CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',  # Vite dev server default port
]

# Configure Django REST framework to use JWT authentication as the default method.
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


# JWT settings for the Django application using Simple JWT.
# - ACCESS_TOKEN_LIFETIME: The access token is valid for 30 minutes.
# - REFRESH_TOKEN_LIFETIME: The refresh token is valid for 5 days.
# - ROTATE_REFRESH_TOKENS: When set to True, a new refresh token is issued each time the old one is used.
# - BLACKLIST_AFTER_ROTATION: When set to True, the old refresh token is blacklisted after a new one is issued.
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=5),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cuppc_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'cuppc_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/


# The absolute path where Django will collect all static files after running the `collectstatic` command.
# This folder is used to serve static files in production.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# The URL prefix for accessing static files in your project.
# Static files will be served at `https://yourdomain.com/static/` in production.
STATIC_URL = '/static/'

# Additional directories where Django will look for static files during development.
# Typically, this includes your project's custom static files (e.g., CSS, JS, images).
# These files will be collected into STATIC_ROOT during the `collectstatic` process.
STATICFILES_DIRS = [
    BASE_DIR / "static"
]


MEDIA_ROOT = BASE_DIR / "uploads"
MEDIA_URL = "/files/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
