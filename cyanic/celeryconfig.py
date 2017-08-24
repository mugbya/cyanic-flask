# BROKER_URL = 'amqp://guest@localhost//'  # 指定 Broker
# CELERY_RESULT_BACKEND = 'redis://localhost'  # 指定 Backend
# CELERY_TIMEZONE = 'Asia/Shanghai'  # 指定时区，默认是 UTC
# CELERY_TIMEZONE='UTC'

broker_url = 'pyamqp://guest@localhost//'
result_backend = 'redis://localhost'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Shanghai'
enable_utc = True

imports = (
    'cyanic.user.tasks',
    # 'cyanic.user.task2'
)
