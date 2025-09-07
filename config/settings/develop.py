from .base import *
from .database import get_config_database


SECRET_KEY = 'django-insecure-_$zk5d#0dc&c)4fg5sfjm$_vtqr^7vo5-0-a9x7sopa)36^@3n'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = get_config_database()