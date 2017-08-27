from flask import Blueprint, make_response


from cyanic.user.tasks import add
import json

user_bp = Blueprint('user', __name__)


@user_bp.route('/')
def index():
    '''
    response 写成如此模样，只有是为了swagger 在线访问跨域
    :return:
    '''
    res = add.delay(4, 4)
    res.backend  # <celery.backends.redis.RedisBackend object at 0x105aac3c8>
    response = make_response(json.dumps({'task_id': res.id}))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, DELETE, PUT, PATCH, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, api_key, Authorization'
    return response


@user_bp.route('/<task_id>/')
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
    response = make_response(json.dumps(res))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, DELETE, PUT, PATCH, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, api_key, Authorization'
    return response
