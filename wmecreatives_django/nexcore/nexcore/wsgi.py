"""WSGI config for nexcore project."""
import os
from django.core.handlers.wsgi import WSGIHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexcore.settings')

def application(environ, start_response):
    return WSGIHandler()(environ, start_response)
