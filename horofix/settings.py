"""
Django settings for horofix project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g68=@==ntced@yg8d&7)!a_4910_t6^=2qd_j%1&$3(odtcv0l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #  'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'horofixapp',
    'channels',
    'crispy_forms'
    
]
CRISPY_TEMPLATE_PACK='bootstrap4'
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


ROOT_URLCONF = 'horofix.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'],
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

# WSGI_APPLICATION = 'horofix.wsgi.application'
ASGI_APPLICATION = 'horofix.asgi.application'




# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

# settings.py

# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'anittarosejoseph2024a@mca.ajce.in'  # Replace with your Gmail email
EMAIL_HOST_PASSWORD = 'dzbfspovlxdrnvjn'



# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#STATIC_URL = 'static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
        # 'CONFIG': {
        #     'hosts': [('127.0.0.1', 6379)],
        # }
    }
}


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'index'
LOGOUT_URL ='index'
LOGOUT_REDIRECT_URL= 'index'

# settings.py
AUTH_USER_MODEL = 'horofixapp.CustomUser'

# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# settings.py

RAZOR_KEY_ID = 'rzp_test_CWNbERskB9qZzi'
RAZOR_KEY_SECRET = '2G7smLq92kbrLngjyFTrFkVd'




SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_NAME = 'sessionid'
#SESSION_COOKIE_SECURE = True  # Set to True in production for HTTPS
#SESSION_COOKIE_HTTPONLY = True
#SESSION_COOKIE_SAMESITE = 'Lax'
SESSION_COOKIE_AGE = 600 # 2 weeks
#SESSION_SAVE_EVERY_REQUEST = False
#SESSION_EXPIRE_AT_BROWSER_CLOSE = False
# LOGIN_URL='login'


# JAZZMIN_SETTINGS = {
#     "show_ui_builder" : True
# }


# settings.py



# settings.py

# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': [
#             'profile',
#             'email',
#         ],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         },
#         'APP': {
#             'client_id': '904247176717-jhqga4eb0ion7126ettmh6pr2vfvp6vd.apps.googleusercontent.com',  # Replace with your actual client ID
#             'secret': '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',  # Replace with your actual client secret
#             # 'key': ''
# }}
# }


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
 
]



# SOCIALACCOUNT_LOGIN_ON_GET=True
# django_project/settings.py
SITE_ID = 1


SOCIALACCOUNT_LOGIN_ON_GET=True

# AUTHENTICATION_BACKENDS = [
#     'allauth.account.auth_backends.AuthenticationBackend'
# ]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'APP': {
            'client_id': '636553351382-srspu6aj8ev6s13qppikrqd6k5pcc4gu.apps.googleusercontent.com',
            'secret': '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',
        }
    }
}