"""
Django settings for ecommerce2 project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #add settings as dedicated folder

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u(+p48v^a25q!d6lrc3oou)_%v%xwj^xc*)5f_t=(iefi278m('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ADMINS = (
    ('countrysidedog', 'csdog@countrysidedog.com'),
)

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
	'newsletter',
    'crispy_forms',
    'registration',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ecommerce2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'ecommerce2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "static_root")
STATIC_ROOT = os.path.join(BASE_DIR, "static_in_env", "static_root")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static_in_pro", "our_static"),
    #os.path.join(BASE_DIR, "static_in_env"),
    #'/var/www/static/',
)

MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_in_env", "media_root")
MEDIA_ROOT = os.path.join(BASE_DIR, "static_in_env", "media_root")

print "base dir" + BASE_DIR
print "STATIC_ROOT" + STATIC_ROOT
print STATICFILES_DIRS

try:
    import settings_security
    EMAIL_HOST_USER = settings_security.USER_NAME
    EMAIL_HOST_PASSWORD = settings_security.USER_PWD
    DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
except:
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    DEFAULT_FROM_EMAIL = ''

EMAIL_HOST = 'smtp.sina.com'
EMAIL_PORT = 25
EMAIL_USE_TLS = True

'''
EMAIL_HOST = 'smtp.sina.com'
EMAIL_PORT = 25

EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 465

EMAIL_HOST = 'smtp.exmail.qq.com'
EMAIL_PORT = 465
'''




#Crispy FORM TAGs SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#DJANGO REGISTRATION REDUX SETTINGS
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
REGISTRATION_EMAIL_SUBJECT_PREFIX = '[Django Registration ecommerce2]'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SEND_ACTIVATION_EMAIL = True

