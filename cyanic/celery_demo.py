from celery import Celery

app = Celery('celery_demo', backend='amqp', broker='amqp://guest@localhost//')


@app.task
def add(x, y):
    return x + y


