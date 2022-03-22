from flask import Flask

from app.api import api
from app.models import db


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.register_blueprint(api)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
