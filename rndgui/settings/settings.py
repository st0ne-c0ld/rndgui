"""
Django settings for rndgui project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from pymongo import MongoClient
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from rndgui.context_processors import get_version

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.dirname(BASE_DIR)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@og4(j(*5s^_pn=fgg%tq%tn84^-%c-^zx^3qck0v9a=fxnb4a'

# Application definition

INSTALLED_APPS = [
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'acm.apps.AcmConfig',
    'prd.apps.PrdConfig',
    'raven.contrib.django.raven_compat',
    'bootstrap3',
    'simple_history',
    'django_extensions',
    'cat',
    'envrnmnt',
    'django_celery_results',
    'django_celery_beat',
    'jra',
    'rest_framework',
    'rpt',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'rndgui.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates')],
        # 'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'rndgui.context_processors.set_version',
            ],
            'loaders': [
                'admin_tools.template_loaders.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader'
            ],
        },
    },
]

WSGI_APPLICATION = 'rndgui.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = '/login/'

# service discovery
PRODUCT_URL = 'http://sv2-web.bt.bpc.in:9090/restful/product'

# Raven settings


RAVEN_CONFIG = {
    'dsn': 'http://f823ca859c9d49ae91de2e2d3a6bec99:e89d8698d6e949929c4bb0c503191da4@sv2-web.bt.bpc.in:9000/9',
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': get_version(),
}

CELERYD_HIJACK_ROOT_LOGGER = False

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'main_formatter': {
            'format': '%(levelname)s:%(name)s: %(message)s '
                      '(%(asctime)s; %(filename)s:%(lineno)d)',
            'datefmt': "%Y-%m-%d %H:%M:%S",
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue'
        }
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'production_file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/rndgul-app.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 7,
            'formatter': 'verbose',
            'filters': ['require_debug_false'],
        },
        'debug_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/main_debug.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 7,
            'formatter': 'main_formatter',
            'filters': ['require_debug_true'],
        },
        'null': {
            "class": 'logging.NullHandler',
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console', 'sentry'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['null', ],
        },
        'py.warnings': {
            'handlers': ['null', ],
        },
        '': {
            'handlers': ['console', 'production_file', 'debug_file', ],
            'level': "DEBUG",
        },
        'raven': {
            'level': 'WARNING',
            'handlers': ['sentry', 'production_file', ],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'WARNING',
            'handlers': ['sentry', 'production_file'],
            'propagate': False,
        }
    }
}

# jira credential
JIRA_USER = 'jira-system'
JIRA_PASS = '3WqOGzrj9G'

# Celery common
CELERY_RESULT_BACKEND = 'django-db'

ADMINS = [('Sergey Dorontsov', 'dorontcov@bpcbt.com'), ('Evgeniy Kryukov', 'krukov@bpcbt.com')]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'PAGE_SIZE': 10
}

# Init MongoDB client
MONGO_CLIENT = MongoClient("mongodb://sv2-web.bt.bpc.in:27017,sv2.bpc.in:27017,sv2-web2.bt.bpc.in:27017", connect=False)
