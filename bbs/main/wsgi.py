"""
WSGI config for bbs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from main.middleware.restrict_access import RestrictAccessMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bbs.settings')

application = get_wsgi_application()
