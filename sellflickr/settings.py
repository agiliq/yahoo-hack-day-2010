DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

AUTHENTICATION_BACKENDS  = ('django.contrib.auth.backends.ModelBackend',
                            'flickrimporter.backends.FlickrBackend',)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'subdomains.middleware.GetSubdomainMiddleware'
)

ROOT_URLCONF = 'urls'

import os
this_dir = os.path.dirname('__file__')

TEMPLATE_DIRS = (
    os.path.join(this_dir,'templates')
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

#Please override this in local settings for everything to work properly
BASE_SITE = 'flickrcommerce.com'
MAIN_SITE = 'www.flickrcommerce.com'
REDIRECT_SITE = MAIN_SITE

PAYPAL_API_USER = "probiz_1273571007_biz_api1.uswaretech.com"
PAYPAL_API_KEY = "LJKRH4CWWE6JTNSN"
PAYPAL_API_SIG = "ADZb7XvwG3K4qw8AuQOMhbhAZ-6HACL1wp2xcDPWwMcjXnxuQVPhrCGy"

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    #'south',
    'flickrimporter',
    'flickrpayments',
    'subdomains',
    'subdomain_admin',
    'grappelli',
    'sampleblog',
    'paypal.standard.ipn',
    'sitewide',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

import os

LOGIN_URL = "/flickr/login/start/"

PROJECT_ROOT = os.path.dirname(__file__)

MEDIA_ROOT =  os.path.join(PROJECT_ROOT, 'media/')
ADMIN_MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'admin-media/')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin-media/'

PAYPAL_RECEIVER_EMAIL = ""

try:
    from localsettings import *
except:
    print "No local settings"
