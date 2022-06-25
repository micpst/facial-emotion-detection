from json import dumps
from flask_socketio import emit

from app import socketio


@socketio.on('upload')
def handle_upload(json=None):
    pass


@socketio.on_error()
def handle_error(exc):
    emit('error', {'message': str(exc)})
