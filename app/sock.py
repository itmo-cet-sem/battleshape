import json
from flask import request
from flask_socketio import emit

from . import socketio
from .memory import redis


@socketio.on('joined')
def joined(data):
    data = json.loads(data)
    coordinates = data['coordinates']
    user_id = request.sid
    data = {'coordinates': coordinates}
    redis.set(user_id, json.dumps(data))
    response = {'user_id': user_id, 'data': data}
    emit('joined', response)


@socketio.on('move')
def moved(data):
    user_id = request.sid
    data = json.loads(data)
    coordinates = data['coordinates']
    redis.set(user_id, json.dumps(coordinates))
    response = [{'user_id': k, 'data': json.loads(redis.gХet(k))} for k in
                redis.keys(f'^(?!{user_id})$')]
    emit('moved', response)
