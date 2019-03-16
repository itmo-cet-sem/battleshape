from flask import Flask
from flask_socketio import SocketIO

from .config import Config

app = Flask(__name__, static_folder='../client/build')
app.config.from_object(Config)
socketio = SocketIO(app, message_queue=app.config.get('RABBITMQ_URL', app.config.get('REDIS_URL')))

if __name__ == '__main__':
    socketio.run(app)
