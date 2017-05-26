from settings import *

DEBUG = False
AUTH_URL = "http://sv2-web.bt.bpc.in/auth/"

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gui',
        'USER': 'gui',
        'PASSWORD': 'gui1',
        'HOST': 'rnd-pg.bt.bpc.in',
        'PORT': '5432',
    }
}
ALLOWED_HOSTS = ["sv2-web.bt.bpc.in", " 10.7.33.73"]

STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# Email
EMAIL_HOST = 'bpcrelay1.bpc.in'
DEFAULT_FROM_EMAIL = 'svtools@bpcbt.com'
EMAIL_SUBJECT_PREFIX = '[SVTools] '
EMAIL_HOST_USER = 'svtools'
EMAIL_HOST_PASSWORD = 'R7xdEp3Y'
