import os
import logging
from logging.config import dictConfig

DEBUG = False
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# -----celery config
# BROKER_URL = 'amqp://dongwm:123456@localhost:5672/web_develop'  # 使用RabbitMQ作为消息代理
# CELERY_BROKER_URL = 'amqp://dongwm:123456@localhost:5672/web_develop'  # 使用RabbitMQ作为消息代理
CELERY_BROKER_URL = 'amqp://guest@localhost//'  # 使用RabbitMQ作为消息代理

# CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'  # 把任务结果存在了Redis
CELERY_RESULT_BACKEND = 'redis://localhost'  # 把任务结果存在了Redis

CELERY_TASK_SERIALIZER = 'msgpack'  # 任务序列化和反序列化使用msgpack方案

CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果一般性能要求不高，所以使用了可读性更好的JSON

CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  # 任务过期时间，不建议直接写86400，应该让这样的magic数字表述更明显

# CELERY_ACCEPT_CONTENT = ['json', 'msgpack']  # 指定接受的内容类型
CELERY_ACCEPT_CONTENT = ['json']  # 指定接受的内容类型
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# ----- log config ------
logging_config = dict(
    version=1,
    formatters={
        'default': {
            'format': '%(asctime)s %(levelname)-8s %(name)-15s %(message)s'
        }
    },
    filter={
    },
    handlers={
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': logging.INFO
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': BASE_DIR + '/log/all.log',
            'formatter': 'default',
            'level': logging.INFO
        },
    },
    loggers={
        'flask': {
            'handlers': ['file'],
            'level': logging.INFO,
            "encoding": "utf8"
        },
        'db': {
            'handlers': ['file'],
            'level': logging.INFO,
            "encoding": "utf8"
        },
        'app': {
            'handlers': ['file'],
            'level': logging.INFO,
            "encoding": "utf8"
        },
    }
)

dictConfig(logging_config)

try:
    from local_config import *
except ImportError:
    pass
