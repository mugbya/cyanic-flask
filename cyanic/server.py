from flask import Flask
import logging

logger = logging.getLogger('app')

app = Flask(__name__)
app.config.from_object('config')


# @app.before_request
# def before_request():
#     g.db = connect_db()
#
#
# @app.teardown_request
# def teardown_request(exception):
#     g.db.close()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about')
def about():
    return 'aaa!'

if __name__ == '__main__':
    try:
        app.run(debug=app.debug)
    except Exception as e:
        logger.exception(e)
