import json
from flask import request
from flask_socketio import emit

from app.calculation import calculate_lives

from . import socketio
from .memory import redis


@socketio.on('joined')
def joined(data):
    user_id = request.sid
    data = json.loads(data)
    data['lives'] = calculate_lives(data['shape'])
    redis.set(user_id, json.dumps(data))
    response = {'user_id': user_id, 'data': data}
    emit('joined', response)


@socketio.on('move')
def moved(data):
    user_id = request.sid
    redis.set(user_id, data)
    response = [{'user_id': k, 'data': json.loads(redis.get(k))} for k in redis.keys(f'^(?!{user_id})$')]
    emit('moved', response)
