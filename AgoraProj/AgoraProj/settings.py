"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-=(2ebjep4^#sc*w-hjb$#ha(j&85ade9b^^*gont52#1bzrh+v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.vercel.app']

SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    'Agora',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'imagekit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]


ROOT_URLCONF = 'AgoraProj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

WSGI_APPLICATION = 'AgoraProj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
import dj_database_url
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES["default"] = dj_database_url.parse("postgres://glow_database_user:AwfcBAa5OeuT06PLHVqvapspu5iaPGOV@dpg-cp5kvs8cmk4c73f44mrg-a.oregon-postgres.render.com/glow_database")


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Manila'

USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '963977549759-s4h9lvm05kq4gkkd00g7scm19at9q6mc.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
            'https://www.googleapis.com/auth/userinfo.profile', 
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_LOGIN_ON_GET=True

IMAGEKIT_DEFAULT_CACHEFILE_BACKEND = 'imagekit.cachefiles.backends.Simple'
IMAGEKIT_CACHEFILE_DIR = 'cache'

from dotenv import load_dotenv
load_dotenv()

IMAGEKIT_PUBLIC_KEY = os.environ.get("IMAGEKIT_PUBLIC_KEY")
IMAGEKIT_PRIVATE_KEY = os.environ.get("IMAGEKIT_PRIVATE_KEY")
IMAGEKIT_URL_ENDPOINT = os.environ.get("IMAGEKIT_URL_ENDPOINT")

DATA_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024  

