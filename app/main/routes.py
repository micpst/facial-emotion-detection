import base64
from http import HTTPStatus
from typing import Tuple, Dict, Union, List

import cv2 as cv
import numpy as np
from flask import render_template, request, abort, jsonify, Response

from app import model, face_cascade
from app.main import main_bp


@main_bp.route('/', methods=['GET'])
def index() -> Tuple[str, int]:
    return render_template('index.html'), \
           HTTPStatus.OK


@main_bp.route('/api/image', methods=['POST'])
def classify() -> Response:
    url = request.json.get('dataURL', '')
    data = url.split(',')
    if len(data) != 2:
        abort(HTTPStatus.BAD_REQUEST)

    image = base64.b64decode(data[1])
    image = np.frombuffer(image, dtype=np.uint8)
    image = cv.imdecode(image, flags=0)

    faces = face_cascade.detectMultiScale(image, 1.02, 1)
    faces = [list(map(int, face)) for face in faces]
    return jsonify([{'x': x, 'y': x, 'w': w, 'h': h} for (x, y, w, h) in faces])
