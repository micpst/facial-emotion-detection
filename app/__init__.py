from typing import Optional

from flask import Flask
from cv2 import CascadeClassifier
from tensorflow.python.keras.models import Model, load_model


model: Optional[Model] = load_model('tmp/model.h5')
face_cascade: Optional[CascadeClassifier] = CascadeClassifier('tmp/haarcascade_frontalface.xml')


def create_app(config_name: str) -> Flask:
    """
    Application factory
    """
    app: Flask = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f'app.config.{config_name.capitalize()}Config')

    with app.app_context():
        from app.main import main_bp
        app.register_blueprint(main_bp)

    return app
