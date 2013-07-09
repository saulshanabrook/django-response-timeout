from django.test import TestCase
from django.test.client import Client


class CacheMiddlewareTest(TestCase):
    def test_overrides_initial(self):
        c = Client()
        response = c.get('')
        self.assertEqual(
            response['Cache-Control'],
            'max-age=2'
        )

    def test_overrides_cached_version(self):
        c = Client()
        c.get('/')
        response = c.get('/')
        self.assertEqual(
            response['Cache-Control'],
            'max-age=2'
        )
