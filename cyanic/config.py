import os
import logging
from logging.config import dictConfig

DEBUG = False
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

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
