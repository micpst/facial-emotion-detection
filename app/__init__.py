from typing import Optional

from flask import Flask
from flask_socketio import SocketIO
from tensorflow.python.keras.models import Model, load_model


sio: SocketIO = SocketIO(path='/socket')
model: Optional[Model] = load_model('tmp/model.h5')


def create_app(config_name: str) -> Flask:
    """
    Application factory
    """
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f'app.config.{config_name.capitalize()}Config')

    sio.init_app(app)

    with app.app_context():
        from app.main import main_bp
        app.register_blueprint(main_bp)

    return app
