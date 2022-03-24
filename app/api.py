from flask import Blueprint, jsonify, request
from werkzeug import Response

from app.exceptions import InsufficientFunds, InvalidParams
from app.services import CryptoService, TransactionService, UserService

api = Blueprint('api', __name__)


@api.get('/users')
def fetch_users() -> Response:
    users = UserService.get_all()

    return jsonify(users)


@api.get('/users/<int:user_id>')
def get_user(user_id: int) -> Response:
    user = UserService.get_by_id(user_id)
    return jsonify(user)


@api.post('/users')
def create_user() -> str:
    name = request.args.get('name')

    if not name:
        raise InvalidParams()

    UserService.create(name=name)

    return 'user successfully created'


@api.patch('/users/<int:user_id>/crypto-currencies')
def add_user_crypto(user_id: int) -> str:
    crypto_id = request.args.get('crypto_id', type=int)
    crypto_count = request.args.get('crypto_count', type=int)

    if not crypto_count or not crypto_id:
        raise InvalidParams()

    try:
        UserService.buy_crypto(user_id=user_id, crypto_id=crypto_id, count=crypto_count)
        return 'success'
    except InsufficientFunds:
        return 'error, insufficient funds'


@api.delete('/users/<int:user_id>/crypto-currencies')
def remove_user_crypto(user_id: int) -> str:
    crypto_id = request.args.get('crypto_id', type=int)
    crypto_count = request.args.get('crypto_count', type=int)

    if not crypto_count or not crypto_id:
        raise InvalidParams()

    try:
        UserService.sell_crypto(
            user_id=user_id, crypto_id=crypto_id, count=crypto_count
        )

        return 'success'
    except InsufficientFunds:
        return 'error, insufficient funds'


@api.get('/crypto-currencies')
def fetch_crypto_currencies() -> Response:
    crypto_currencies = CryptoService.get_all()

    return jsonify(crypto_currencies)


@api.get('/crypto-currencies/<int:crypto_id>')
def get_crypto(crypto_id: int) -> Response:
    crypto = CryptoService.get_by_id(crypto_id)

    return jsonify(crypto)


@api.post('/crypto-currencies')
def create_crypt() -> str:
    name = request.args.get('name')
    value = request.args.get('value')

    if not name or not value:
        raise InvalidParams()

    CryptoService.create(name=name, value=value)

    return 'crypt successfully created'


@api.get('/transactions')
def fetch_transactions() -> Response:
    transactions = TransactionService.get_all()

    return jsonify(transactions)
