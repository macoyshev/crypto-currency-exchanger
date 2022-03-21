from flask import Flask

from app import models
from app.database import engine


def create_app():
    from app.api import api

    models.Base.metadata.create_all(engine)

    app = Flask(__name__)
    app.register_blueprint(api)

    return app
