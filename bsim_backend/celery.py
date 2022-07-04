import os

from celery import Celery


app = Celery('bsim_backend')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {}
