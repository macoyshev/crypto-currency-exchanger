from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


@dataclass
class User(db.Model):
    name: str
    id: int = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), unique=True, nullable=False)


@dataclass
class CryptoCurrency(db.Model):
    value: float
    name: str
    id: int = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), unique=True, nullable=False)
    value = db.Column(db.DECIMAL(19, 4), nullable=False)
