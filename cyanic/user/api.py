from flask import Blueprint

# from cyanic.celery_app.tasks import add
# from cyanic.celery_app.main import add
# from cyanic.celery_demo import add
from cyanic.user.tasks import add
import time

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def index():
    '''

    :return:
    '''
    res = add.delay(4, 4)
    # print(res.ready())
    #
    # time.sleep(5)
    #
    # print(res.ready())

    return 'user index'
