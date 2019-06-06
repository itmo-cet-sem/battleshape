import os
from flask import send_from_directory, Blueprint, jsonify

front = Blueprint('frontend', __name__,
                  url_prefix='/',
                  static_folder='../unity/Build')


@front.route('/', defaults={'path': ''})
@front.route('/<path:path>')
def serve_static(path):
    if path != '' and os.path.exists(f'{front.static_folder}/{path}'):
        return front.send_static_file(path)
    else:
        return send_from_directory(front.static_folder, 'index.html')


@front.route('/ping')
def ping():
    return jsonify('pong'), 200
