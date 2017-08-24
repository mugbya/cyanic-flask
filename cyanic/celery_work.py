from __future__ import absolute_import
from celery import Celery
from .config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

# app = Celery('proj', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
# app = Celery('celery_work', include=['user.tasks'])
app = Celery('celery_work', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND, include=['cyanic.user.tasks'])


app.conf.update(
    CELERY_TASK_SERIALIZER='json',
    CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
    CELERY_RESULT_SERIALIZER='json',
    CELERY_EVENT_SERIALIZER='json',
    CELERY_TIMEZONE='Europe/Oslo',
    CELERY_ENABLE_UTC=True,
)

# app.config_from_object('config')
# app.config_from_object('cyanic.config')

