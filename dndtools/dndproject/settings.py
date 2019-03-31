"""
Django settings for dndtools project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6yvups)$x1_0_5t*1%f%o668*0lwkwjdp9c6w&4wyu31_-hhx1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dnd',
    # '.',
    # 'south',
    'debug_toolbar',
    'django.contrib.sitemaps',
)

MIDDLEWARE = [
    # added
    # 'dnd.mobile.middleware.MobileMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'pagination.middleware.PaginationMiddleware',
    # default
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF = 'dndtools.urls'
ROOT_URLCONF = 'dndproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['./templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # added stuff
                'dnd.context_processors.unread_news',
                'dnd.context_processors.disable_social',
                'dnd.context_processors.is_mobile',
                'dnd.context_processors.is_admin',
                'dnd.context_processors.menu_constants',
            ],
        },
    },
]

# WSGI_APPLICATION = 'dndtools.wsgi.application'
WSGI_APPLICATION = 'dndproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


ADMINS = (
    ('DnDtools', 'dndtools.eu@gmail.com'),
)

MANAGERS = ADMINS
# TIME_ZONE = 'Europe/Prague'
# LANGUAGE_CODE = 'en-us'
# is media_url even needed?
MEDIA_URL = '/media/'
# STATIC_URL = '/static/'
# USE_I18N = False
# USE_L10N = False
ADMIN_MEDIA_PREFIX = '/media/'


SERVER_EMAIL = 'error@dndtools.eu'

# LOCAL PY

MEDIA_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = (STATIC_DIR, )
SITE_ID = 1

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

RECAPTCHA_PUBLIC = ''


# from dndproject.local import *