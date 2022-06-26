from json import dumps
from flask_socketio import emit

from app import sio


@sio.on('upload')
def handle_upload(json=None):
    pass


@sio.on_error()
def handle_error(exc):
    emit('error', {'message': str(exc)})
