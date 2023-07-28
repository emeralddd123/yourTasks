"""
Django settings for TaskManager project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from decouple import config
#from django.test.runner import DiscoverRunner




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 0

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'emerald-todo.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    
    
    # 3rd party
    'crispy_forms',
    'crispy_bootstrap5',
    'bootstrap5',
    
    
    'allauth',
    'allauth.account', 
    'allauth.socialaccount',   
    'verify_email.apps.VerifyEmailConfig',  
    
    
    #social apps
    'allauth.socialaccount.providers.google',
    
        
    #local Apps
    'accounts',
    'task',
        
]

AUTH_USER_MODEL = 'accounts.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TaskManager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'TaskManager.wsgi.application'


# Database # HEROKU stopped free postgres, thats why i comment the section for it out, the DB have been migrtaed to sqlite3
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'ec2-3-213-228-206.compute-1.amazonaws.com',               #IT SHOULD BE THE HEROKU POSGRES HOST  BEFORE PUSHING TO PRODUCTION
        'PORT': 5432,
    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'taskAppDB', # This is where you put the name of the db file. 
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

#DATE_INPUT_FORMATS = '%Y/%m/%d'

DATE_FORMAT = "Y-m-d"

#TIME_INPUT_FORMATS =  '%H:%I'

TIME_FORMAT = "H:i"

USE_L10N = False

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


# # Test Runner Config
# class HerokuDiscoverRunner(DiscoverRunner):
#     """Test Runner for Heroku CI, which provides a database for you.
#     This requires you to set the TEST database (done for you by settings().)"""

#     def setup_databases(self, **kwargs):
#         self.keepdb = True
#         return super(HerokuDiscoverRunner, self).setup_databases(**kwargs)

# # Use HerokuDiscoverRunner on Heroku CI
# if "CI" in os.environ:
#     TEST_RUNNER = "gettingstarted.settings.HerokuDiscoverRunner"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#mwdia directory

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')
#SERVER_MAIL = 'usman<@localhost>'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp-relay.sendinblue.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER =  config('EMAIL_ACCOUNT_NAME')
EMAIL_HOST_PASSWORD = config('EMAIL_ACCOUNT_PASSWORD')



AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = False        #i'll later change this to True
ACCOUNT_EMAIL_VERIFICATION ='optional'     #i'll later change this to mandatory(perfect)/ optional(not advisable)

SESSION_COOKIE_AGE = 12*60*60       #in seconds

ACCOUNT_SESSION_REMEMBER = False


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}


CRISPY_TEMPLATE_PACK = 'bootstrap5'


LOGIN_REDIRECT_URL = 'task:tasks'
ACCOUNT_LOGOUT_REDIRECT_URL = 'task:home'

