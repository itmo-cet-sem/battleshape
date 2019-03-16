import os


class Config:
    PYTHONUNBUFFERED = 0
    FLASK_ENV = os.environ.get('FLASK_ENV')
    DEBUG = True if FLASK_ENV == 'development' else False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_ADMIN_SWATCH = 'cosmo'
    HOST_URL = os.environ.get('HOST_URL', None)
    PROPAGATE_EXCEPTIONS = False
    ERROR_INCLUDE_MESSAGE = False

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    REDIS_URL = os.environ.get('REDIS_URL')
    RABBITMQ_URL = os.environ.get('CLOUDAMQP_URL')
    MONGODB_URI = os.environ.get('MONGODB_URI')
