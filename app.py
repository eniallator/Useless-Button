from flask import Flask, request, send_from_directory
from flask_socketio import SocketIO, emit
import json
from re import match
from os import path

APP = Flask(__name__, static_folder='/static', static_url_path='/static')
SOCKETIO = SocketIO(APP)

USELESS_LOGS = ['App started']

@APP.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')

@SOCKETIO.on('login')
def login():
    emit('logs update', '\n'.join(USELESS_LOGS))

@SOCKETIO.on('button click')
def buttonClicked(msg):
    jsonMsg = json.loads(msg)

    if 'userName' not in jsonMsg or not match(r'^\w+$', jsonMsg['userName']) or len(jsonMsg['userName']) > 20:
        return

    USELESS_LOGS.append(jsonMsg['userName'] + ' pressed the button!')

    if len(USELESS_LOGS) > 25:
        USELESS_LOGS.pop(0)

    emit('logs update', '\n'.join(USELESS_LOGS), broadcast=True)

if __name__ == '__main__':
    # APP.run(host='0.0.0.0', port=3000, debug=True)
    SOCKETIO.run(APP, host='0.0.0.0', port=3000)
