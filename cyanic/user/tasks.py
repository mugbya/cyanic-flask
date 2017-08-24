# from celery_app.main import app
from cyanic.celery_work import app


@app.task
def add(x, y):
    return x + y
