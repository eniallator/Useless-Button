import json
from re import match
from flask import Flask, send_from_directory
from flask_socketio import SocketIO, emit

APP = Flask(__name__, static_folder='/static', static_url_path='/static')
SOCKETIO = SocketIO(APP)

USELESS_LOGS = ['App started']


@APP.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')


@SOCKETIO.on('get logs')
def login():
    emit('logs update', '\n'.join(USELESS_LOGS))


@SOCKETIO.on('button click')
def buttonClicked(msg):
    json_msg = json.loads(msg)

    if 'nickname' not in json_msg or not match(r'^\w+$', json_msg['nickname']) or len(json_msg['nickname']) > 20:
        return

    USELESS_LOGS.append(json_msg['nickname'] + ' pressed the button!')

    if len(USELESS_LOGS) > 25:
        USELESS_LOGS.pop(0)

    emit('logs update', '\n'.join(USELESS_LOGS), broadcast=True)


if __name__ == '__main__':
    SOCKETIO.run(APP, host='0.0.0.0', port=3000)
