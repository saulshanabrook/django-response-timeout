from django.http import HttpResponse
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', lambda request: HttpResponse()),
)
