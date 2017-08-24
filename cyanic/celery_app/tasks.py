from celery_app.main import app
from celery import task

# @app.task
@task
def add(x, y):
    return x + y
