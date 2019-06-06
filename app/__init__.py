from flask import Flask
from flask_socketio import SocketIO

from config import conf

socketio = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config.from_object(conf)

    from app.routes import front
    app.register_blueprint(front)

    from app.memory import redis
    redis.init_app(app)

    socketio.init_app(app,
                      message_queue=app.config.get(app.config['REDIS_URL']),
                      logger=True, engineio_logger=True)
    return app
