from app.models import User, CryptoCurrency
from app.database import Session


class UserService:
    @staticmethod
    def get_all():
        session = Session()
        users = session.query(User).all()

        return users

    @staticmethod
    def create(name):
        user = User(name=name)

        session = Session()
        session.add(user)
        session.commit()
        session.refresh(user)

        return user


class CryptoCurrencyService:
    @staticmethod
    def create(name: str, value: float):
        crypt = CryptoCurrency(name=name, value=value)

        session = Session()
        session.add(crypt)
        session.commit()
        session.refresh(crypt)

        return crypt

    @staticmethod
    def get_all() -> list[str]:
        session = Session()
        crypt_currencies = session.query(CryptoCurrency).all()

        return crypt_currencies
