import datetime
import json
from flask import request
from flask_socketio import emit

from app.calculation import calculate_lives, remove_outdated_coordinates

from . import socketio
from .memory import redis


@socketio.on('joined')
def joined(data):
    user_id = request.sid
    data = json.loads(data)
    data['lives'] = calculate_lives(data['shape'])
    data['coordinates'] = [{
        'datetime': datetime.datetime.utcnow(),
        'position': data['coordinates']
    }, ]
    redis.set(user_id, json.dumps(data))
    response = {'user_id': user_id, 'data': data}
    emit('joined', response)


@socketio.on('move')
def moved(data):
    user_id = request.sid
    data = json.loads(data)
    if len(data['coordinates']) == 3:
        remove_outdated_coordinates(data['coordinates'])

    data['coordinates'].append({
        'datetime': datetime.datetime.utcnow(),
        'position': data['coordinates']
    })
    redis.set(user_id, data)
    response = [{'user_id': k, 'data': json.loads(redis.get(k))} for k in
                redis.keys(f'^(?!{user_id})$')]
    emit('moved', response)
