from typing import Union, Optional

import simplejson

from app.database import Session
from app.models import CryptoCurrency, CryptoCurrencySchema, User, UserSchema


class UserService:
    @staticmethod
    def create(username: str):
        with Session() as session:
            user = User(username=username)

            session.add(user)
            session.commit()
            session.refresh(user)

            return user

    @staticmethod
    def get_all():
        with Session() as session:
            users = session.query(User).all()

            return users


class CryptoCurrencyService:
    @staticmethod
    def create(name: str, value: Union[int, float]) -> str:
        with Session() as session:
            crypt = CryptoCurrency(name=name, value=value)
            session.add(crypt)
            session.commit()

            return simplejson.dumps(crypt)

    @staticmethod
    def get_all() -> list[str]:
        with Session() as session:
            crypto_currencies = session.query(CryptoCurrency).all()

            return [CryptoCurrencySchema().dumps(crypt) for crypt in crypto_currencies]
