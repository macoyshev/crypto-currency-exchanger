import json

from flask import Blueprint, request

from app.services import CryptoCurrencyService, UserService
from app.utils import get_json_from

api = Blueprint('api', __name__)


@api.get('/users')
def fetch_users():
    users = UserService.get_all()

    return get_json_from(users)


@api.post('/users')
def create_user():
    name = request.form.get('username')
    new_user = UserService.create(username=name)

    print(new_user)

    return get_json_from(new_user)


@api.get('/crypto-currencies')
def fetch_crypto_currencies():
    crypto_currencies = CryptoCurrencyService.get_all()

    return json.dumps([crypt.as_dict() for crypt in crypto_currencies])


@api.post('/users')
def create_crypto_currencies():
    name = request.form.get('name')
    value = request.form.get('value', type=float)

    crypt = CryptoCurrencyService.create(name=name, value=value)

    return json.dumps(crypt.as_dict())
