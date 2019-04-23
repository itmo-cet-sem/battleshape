from . import socketio
from .model.usermanager import session
from flask_socketio import emit
import json
import base64


@socketio.on('hello')
def say_hi():
    user_id = session.hello()
    message = {
        'status': 200,
        'message': 'F*ck the python',
        'user_id': user_id
    }
    emit('hello', json.dumps(message, ensure_ascii=False).encode('utf-8'))


@socketio.on('new_session')
def create_session():
    session.new_session()
    emit('new_session', 'OK')


@socketio.on('broadcast')
def broadcast():
    message = {
        'status': 200,
        'message': 'OK',
        'enemies_data': session.to_json()
    }
    ascii_str = json.dumps(message, ensure_ascii=False).encode('ascii')
    emit('broadcast', base64.b64encode(ascii_str), broadcast=True)
