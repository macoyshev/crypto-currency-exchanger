from app.database import Session
from app.models import CryptoCurrency, User


class UserService:
    @staticmethod
    def create(username):
        user = User(username=username)

        with Session() as session:
            session.add(user)
            session.commit()

        return user

    @staticmethod
    def get_all():
        with Session() as session:
            return session.query(User).all()


class CryptoCurrencyService:
    @staticmethod
    def create(name, value):
        crypto_currency = CryptoCurrency(name=name, value=value)

        with Session() as session:
            session.add(crypto_currency)
            session.commit()

            return crypto_currency

    @staticmethod
    def get_all():
        with Session() as session:
            return session.query(CryptoCurrency).all()
