import django

from os import path


SECRET_KEY = 'not secret'
INSTALLED_APPS = ('response_timeout', 'test')
TEMPLATE_DEBUG = DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'response_timeout.db',
    },
}
ROOT_URLCONF = 'test.urls'

# Testing
if django.VERSION[:2] < (1, 6):
    INSTALLED_APPS += ('discover_runner',)
    TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = path.dirname(path.dirname(__file__))

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'response_timeout'
    },
}
MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'response_timeout.middleware.SetCacheTimeoutMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_KEY_PREFIX = ''
CACHE_MIDDLEWARE_SECONDS = 1

RESPONSE_CACHE_SECONDS = 2
