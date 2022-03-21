from flask import Blueprint, request

from app.services import UserService


api = Blueprint('api', __name__)


@api.get('/users')
def fetch_users():
    return str(UserService.get_all())


@api.post('/users')
def create_user():
    name = request.form.get('username')
    new_user = UserService.create(username=name)

    return f'created'
