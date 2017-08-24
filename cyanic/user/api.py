from flask import Blueprint

# from cyanic.celery_app.tasks import add
# from cyanic.celery_app.main import add
# from cyanic.celery_demo import add
from cyanic.user.tasks import add
import json

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def index():
    '''

    :return:
    '''
    res = add.delay(4, 4)
    return json.dumps({'task_id': res.id})


@user_bp.route('/<task_id>')
def get_result_by_task_id(task_id):
    '''

    :param task_id:
    :return:
    '''
    task = add.AsyncResult(task_id)
    res = {
        'state': task.state,
        'result': task.result
    }
    return json.dumps(res)
