"""
ASGI config for mysite_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
import channels.asgi

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite_project.settings')
channel_layer = channels.asgi.get_channel_layer()
