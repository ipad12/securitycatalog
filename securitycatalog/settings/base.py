"""
Django settings for securitycatalog project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMP_DIR = os.path.join(BASE_DIR, 'templates')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1of$vo^zr9j%@-nngg8qnpae2ws#!8nhw%x9il^rt5+h%kuty$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

ALLOWED_HOSTS = ['securitycatalog.nexuspresales.com']


# Application definition

INSTALLED_APPS = [
    'security.apps.SecurityConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_saml2_auth',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'securitycatalog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMP_DIR],
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

WSGI_APPLICATION = 'securitycatalog.wsgi.application'


#ELASTIC_APM = {
  # Set required service name. Allowed characters:
  # a-z, A-Z, 0-9, -, _, and space
#  'SERVICE_NAME': 'Security Catalog Django Monitoring',

  # Use if APM Server requires a token
#  'SECRET_TOKEN': 'dd93KhSxTLp43Y6XyV',

  # Set custom APM Server URL (default: http://localhost:8200)
#  'SERVER_URL': 'https://7cd209d56d3e42bc9741739354ea8817.apm.ap-southeast-1.aws.cloud.es.io:443',
#    
#    'DEBUG':  True,
#}

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {   
        'default': {      
            'ENGINE': 'djongo',      
            'NAME': 'security_catalog',
            'HOST' : 'mongodb+srv://adpadilla:zpAsrf1RJQL19f9C@securitycatalogue-ajulm.mongodb.net/test?retryWrites=true&w=majority',
            'USER' : 'adpadilla',
            'PASSWORD' : 'zpAsrf1RJQL19f9C',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_ZONE = 'Asia/Manila'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
STATICFILES_DIRS = [
    'security/static/'
]
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = '/accounts/login'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s HKT [%(levelname)s] %(name)s: %(message)s' #You may need to specify the timezone here. For example: %(asctime)s CST [%(levelname)s] %(name)s: %(message)s
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'logging.NullHandler',
        },
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler'
        },
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': '/var/log/django/security_catalog/app.log', # Make sure that this path exists, change as necessary
            'maxBytes': 1024*1024*10, # 10 MB
            'backupCount': 5,
            'formatter':'standard',
        }
    },
    'loggers': {
        'django.db': {
            'handlers': ['default'],
            'level': 'DEBUG', # Set this to ERROR on production hosts since the database logs are very verbose
            'propagate': False, 
        },
        'django.db.backends': {
            'level': 'DEBUG',
            'handlers': ['default'],
            'propagate': False,
        },
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
        'handlers': ['null'],
        'propagate': False,
        },
        'django.request': {
            'handlers': ['default'],
            'level': 'ERROR', # Set this to ERROR on production hosts if you want to avoid lots of warnings for 404 file-not-found notices
            'propagate': False,
        },
    }
}

SAML2_AUTH = {
    # Metadata is required, choose either remote url or local file path
    'METADATA_AUTO_CONF_URL': 'https://dev-251722.okta.com/app/exk19qs6hCy2S7d6u4x6/sso/saml/metadata',
 

    # Optional settings below
    'DEFAULT_NEXT_URL': '/',  # Custom target redirect URL after the user get logged in. Default to /admin if not set. This setting will be overwritten if you have parameter ?next= specificed in the login URL.
    'CREATE_USER': 'TRUE', # Create a new Django user when a new user logs in. Defaults to True.
    'NEW_USER_PROFILE': {
        'USER_GROUPS': [],  # The default group name when a new user logs in
        'ACTIVE_STATUS': True,  # The default active status for new users
        'STAFF_STATUS': True,  # The staff status for new users
        'SUPERUSER_STATUS': False,  # The superuser status for new users
    },
    'ATTRIBUTES_MAP': {  # Change Email/UserName/FirstName/LastName to corresponding SAML2 userprofile attributes.
        'email': 'email',
        'username': 'username',
        'first_name': 'first_name',
        'last_name': 'last_name',
    },
    # Custom URL to validate incoming SAML requests against
    'ENTITY_ID': 'http://securitycatalog.nexuspresales.com/saml2_auth/acs/', # Populates the Issuer element in authn request
    'NAME_ID_FORMAT': 'None', # Sets the Format property of authn NameIDPolicy element
    'USE_JWT': False, # Set this to True if you are running a Single Page Application (SPA) with Django Rest Framework (DRF), and are using JWT authentication to authorize client users
    'FRONTEND_URL': 'https://myfrontendclient.com', # Redirect URL for the client if you are using JWT auth with DRF. See explanation below
}

