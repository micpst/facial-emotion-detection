from http import HTTPStatus
from typing import Tuple

from flask import render_template

from app.main import main_bp


@main_bp.route('/')
def index() -> Tuple[str, int]:
    return render_template('index.html'), \
           HTTPStatus.OK
