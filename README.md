# cyanic-flask

A full (very basic) example of using flask, celery, rabbitmq and  redis to distribute tasks/jobs.


## requirements

- celery==4.1.0
- flask==0.12.2
- redis==2.10.6



## start celery

    cd cyanic-flask
    celery -A cyanic worker -l info
    
## start server

    cd cyanic-flask/cyanic
    python server.py
