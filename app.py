from flask import Flask, request, send_from_directory
from os import path

APP = Flask(__name__, static_folder='/static',static_url_path='/static')

@APP.route('/', methods=['GET'])
def index():
    return send_from_directory('static', 'index.html')

@APP.route('/', methods=['POST'])
def buttonClicked():
    if request.mimetype == 'application/json':
        print(request.json)
    return 'Received request'

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=3000, debug=True)
