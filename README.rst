django-response-timeout
============================

.. image:: https://pypip.in/v/django-response-timeout/badge.png
        :target: https://crate.io/packages/django-response-timeout

.. image:: https://travis-ci.org/saulshanabrook/django-response-timeout.png
    :target: https://travis-ci.org/saulshanabrook/django-response-timeout

``django-response-timeout`` allows you to set the cache time globally for
all responses. It provides a way to override the client side cache time for
the Django `per site`_ caching middleware.

.. _per site: https://docs.djangoproject.com/en/dev/topics/cache/#the-per-site-cache


Installation
------------
Installation is as easy as::

    pip install django-response-timeout


Setup
-----
Add ``response_timeout.middleware.SetCacheTimeoutMiddleware`` and place it
after ``django.middleware.cache.UpdateCacheMiddleware`` so that it will set the
header time first on cached responses.

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        'django.middleware.cache.UpdateCacheMiddleware',
        'response_timeout.middleware.SetCacheTimeoutMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.cache.FetchFromCacheMiddleware',
    )

Then set ``RESPONSE_CACHE_SECONDS`` to the number of seconds each page should
be cached on the front end.

The Django documention does not cohesively describe how your middleware
should be ordered, however `this stackoverflow`_ discussion does a fine job.

.. _this stackoverflow: http://stackoverflow.com/questions/4632323/practical-rules-for-django-middleware-ordering#question


Contributing
------------

If you find issues or would like to see a feature suppored, head over to
the `issues section` and report it. Don't be agraid, go ahead, do it!

.. _issues section: https://github.com/saulshanabrook/django-response-timeout/issues

To contribute code in any form, fork the repository and clone it locally.
Create a new branch for your feature::

    git commit -b feature/whatever-you-like

Then make sure all the tests past (and write new ones for any new features)::

    pip install -e .
    pip install -r requirements-dev.txt
    django-admin.py test --settings=test.settings

Check if the README.rst looks right::

    restview --long-description

Then push the finished feature to github and open a pull request form the branch.

New Release
^^^^^^^^^^^
To create a new release:

1. Add changes to ``CHANGES.txt``
2. Change version in ``setup.py``
3. ``python setup.py register``
4. ``python setup.py sdist upload``
