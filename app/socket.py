from . import socketio


# ex.
@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))
