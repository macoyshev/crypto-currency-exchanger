from flask import Flask

from app import models
from app.database import engine
from app.api import api


def create_app() -> Flask:

    models.Base.metadata.create_all(engine)

    app = Flask(__name__)
    app.register_blueprint(api)

    return app
