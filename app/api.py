from flask import Blueprint, jsonify, request
from werkzeug import Response

from app.services import UserService, CryptoCurrencyService

api = Blueprint('api', __name__)


@api.get('/users')
def fetch_users() -> Response:
    users = UserService.get_all()

    return jsonify(users)


@api.post('/users')
def create_user() -> Response:
    name = request.form.get('name')

    if not name:
        raise Exception()

    user = UserService.create(name=name)
    return jsonify(user)


@api.get('/crypto-currencies')
def fetch_crypto_currencies() -> Response:
    crypto_currencies = CryptoCurrencyService.get_all()

    return jsonify(crypto_currencies)


@api.post('/crypto-currencies')
def create_crypt() -> Response:
    name = request.form.get('name')
    value = request.form.get('value', type=float)

    if not name or not value:
        raise Exception()

    crypt = CryptoCurrencyService.create(name=name, value=value)

    return jsonify(crypt)
