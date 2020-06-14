"""
ASGI config for mysite_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import django
from channels.layers import get_channel_layer
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite_project.settings')
django.setup()
application = get_default_application()
channel_layer = get_channel_layer()
