import flask
from os import path

APP = flask.Flask(__name__, static_folder='/static',static_url_path='/static')

@APP.route('/')
def index():
    return flask.send_from_directory('static', 'index.html')

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=3000, debug=True)
