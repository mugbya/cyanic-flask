import os

DEBUG = False
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


try:
    from .local_config import *
except ImportError:
    pass


