from flask import Flask
from flask_socketio import SocketIO

socketio: SocketIO = SocketIO(path='/socket')


def create_app(config_name: str) -> Flask:
    """
    Application factory
    """
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f'app.config.{config_name.capitalize()}Config')

    socketio.init_app(app)

    with app.app_context():
        import app.events as events

    return app
