import base64
from http import HTTPStatus
from typing import Tuple

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
def classify() -> Tuple[Response, int]:
    url = request.json.get('dataURL', '')
    data = url.split(',')
    if len(data) != 2:
        abort(HTTPStatus.BAD_REQUEST)

    image = base64.b64decode(data[1])
    image = np.frombuffer(image, dtype=np.uint8)
    image = cv.imdecode(image, flags=0)

    results = []
    emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    faces = face_cascade.detectMultiScale(image, 1.03, 5)
    for (x, y, w, h) in faces:
        roi = image[y:y + h, x:x + w]
        roi = cv.resize(roi, (48, 48))
        roi = np.expand_dims(roi, axis=0)

        predictions = model.predict(roi)
        label = emotions[np.argmax(predictions)]
        score = np.max(predictions) * 100
        results.append({
            'x': int(x),
            'y': int(y),
            'w': int(w),
            'h': int(h),
            'label': label,
            'score': int(score)
        })

    return jsonify(results), \
           HTTPStatus.OK
