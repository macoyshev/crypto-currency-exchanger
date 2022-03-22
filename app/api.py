import json

import simplejson
from flask import Blueprint, request

from app.services import CryptoCurrencyService, UserService
from app.utils import get_json_from

api = Blueprint('api', __name__)


@api.get('/users')
def fetch_users() -> str:
    users = UserService.get_all()
    return simplejson.dumps(users)


@api.post('/users')
def create_user() -> str:
    name = request.form.get('username')

    if not name:
        raise Exception()

    user = UserService.create(username=name)

    return get_json_from(user)


@api.get('/crypto-currencies')
def fetch_crypto_currencies() -> str:
    crypto_currencies = CryptoCurrencyService.get_all()

    return get_json_from(crypto_currencies)


@api.post('/crypto-currencies')
def create_crypto_currencies() -> str:
    name = request.form.get('name')
    value = request.form.get('value', type=float)

    if not name or not value:
        raise Exception()

    crypt = CryptoCurrencyService.create(name=name, value=value)

    return get_json_from(crypt)
