from http import HTTPStatus
from typing import Tuple, Any

from flask import render_template

from app.main import main_bp


@main_bp.errorhandler(HTTPStatus.NOT_FOUND)
def handle_not_found_error(e: Any) -> Tuple[str, int]:
    return render_template('page-404.html'), \
           HTTPStatus.NOT_FOUND


@main_bp.errorhandler(Exception)
def handle_internal_server_error(e: Any) -> Tuple[str, int]:
    return render_template('page-500.html'), \
           HTTPStatus.INTERNAL_SERVER_ERROR
