from celery import Celery

from celery_config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

app = Celery('main', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)
# app = Celery('celery_app', include=['celery_app.tasks'])

# app.config_from_object('celery_app.celery_config')


@app.task
# @task
def add(x, y):
    return x + y


if __name__ == '__main__':

    app.start()

