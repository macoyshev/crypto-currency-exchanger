from flask import Blueprint, jsonify, request
from werkzeug import Response

from app.services import CryptoCurrencyService, UserService

api = Blueprint('api', __name__)


@api.get('/users')
def fetch_users() -> Response:
    users = UserService.get_all()

    return jsonify(users)


@api.post('/users')
def create_user() -> str:
    name = request.form.get('name')

    if not name:
        raise Exception()

    UserService.create(name=name)

    return 'user successfully created'


@api.get('/crypto-currencies')
def fetch_crypto_currencies() -> Response:
    crypto_currencies = CryptoCurrencyService.get_all()

    return jsonify(crypto_currencies)


@api.post('/crypto-currencies')
def create_crypt() -> str:
    name = request.form.get('name')
    value = request.form.get('value', type=float)

    if not name or not value:
        raise Exception()

    CryptoCurrencyService.create(name=name, value=value)

    return 'crypt successfully created'
