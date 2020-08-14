import os
from celery import Celery


# Zadayem peremennuyu okrujeniya, soderjashuyu nazvaniye fayla nastroyek nashego proyekta
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_oyden.settings')
app = Celery('django_oyden')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()