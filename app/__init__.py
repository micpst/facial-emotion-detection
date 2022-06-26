from typing import Optional

from flask import Flask
from flask_socketio import SocketIO
from tensorflow.keras.models import model_from_json

sio: SocketIO = SocketIO(path='/socket')
model: Optional[str] = None

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

    # with open('model/structure.json', 'r') as f:
    #     global model
    #     model = model_from_json(f.read())
    #     model.load_weights('model/weights.h5')

    return app
