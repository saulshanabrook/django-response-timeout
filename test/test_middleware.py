from django.test import TestCase
from django.http import HttpResponse, HttpRequest

from response_timeout.middleware import SetCacheTimeoutMiddleware


class SetCacheTimeoutMiddlewareTest(TestCase):
    def test_sets_response(self):
        request = HttpRequest()
        response = HttpResponse()
        response = SetCacheTimeoutMiddleware().process_response(request, response)
        self.assertEqual(
            response['Cache-Control'],
            'max-age=2'
        )
