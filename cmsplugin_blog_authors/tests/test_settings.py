"""Settings that need to be set in order to run the tests."""
import os

DEBUG = True
FILER_DEBUG = True

SITE_ID = 1

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

USE_I18N = True

ROOT_URLCONF = 'cmsplugin_blog_authors.tests.urls'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../../static/')
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), '../../media/')

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), 'test_static'),
)

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), '../templates'),
)

COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__), 'coverage')

COVERAGE_MODULE_EXCLUDES = [
    'tests$', 'settings$', 'urls$', 'locale$', 'cms$', 'cmsplugin_blog$',
    'migrations', 'fixtures', 'admin$', 'django_extensions',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
)

EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django_nose',
    'sekizai',
    'menus',
    'mptt',
    'tagging',
    'filer',
    'people',
]

# If we leave this in EXTERNAL_APPS it will hide this app from coverage
NO_COVERAGE_APPS = [
    'cms',
    'cmsplugin_blog',
]

INTERNAL_APPS = [
    'cmsplugin_blog_authors.tests.test_app',
    'cmsplugin_blog_authors',
]

INSTALLED_APPS = EXTERNAL_APPS + NO_COVERAGE_APPS + INTERNAL_APPS

COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS

SECRET_KEY = 'foobar'

CMS_SOFTROOT = True
CMS_PERMISSION = False
CMS_SEO_FIELDS = True
CMS_MENU_TITLE_OVERWRITE = True
CMS_FRONTEND_LANGUAGES = ('en', 'de', )
CMS_TEMPLATES = (
    ('standard.html', 'Standard'),
)

JQUERY_JS = 'https://ajax.googleapis.com/ajax/libs/jquery/1.4.4/jquery.min.js'
JQUERY_UI_JS = (
    'https://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/jquery-ui.min.js')
JQUERY_UI_CSS = (
    'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.12/themes/smoothness/'
    'jquery-ui.css')
