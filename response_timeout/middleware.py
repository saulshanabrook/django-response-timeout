from django.conf import settings
from django.utils.cache import patch_response_headers


class SetCacheTimeoutMiddleware(object):
    """
    Request-phase middleware that sets the timeout of each response based on
    the RESPONSE_CACHE_SECONDS

    If using with UpdateCacheMiddleware, must be placed after so that it sets
    the timeout before the cache is updated with the response.
    """
    def process_response(self, request, response):
        timeout = settings.RESPONSE_CACHE_SECONDS
        patch_response_headers(response, timeout)
        return response
