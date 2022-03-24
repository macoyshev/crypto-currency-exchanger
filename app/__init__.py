from flask import Flask

from app.api import api
from app.database import create_db


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(api)

    create_db()

    return app
