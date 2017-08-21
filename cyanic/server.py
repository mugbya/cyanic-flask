from flask import Flask


app = Flask(__name__)
app.config.from_object('config')
#
# app.config.from_pyfile(app.config['BASE_DIR']+'/instance/config.py')

print(app.config['DEBUG'])


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/about')
def about():
    return 'aaa!'

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'], )
