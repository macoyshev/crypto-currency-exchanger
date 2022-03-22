from app.database import Session
from app.models import CryptoCurrency, User, UserSchema, CryptoCurrencySchema


class UserService:
    @staticmethod
    def create(username):
        user = User(username=username)
        user_schema = UserSchema()

        session = Session()
        session.add(user)
        session.commit()

        return user_schema.dumps(user)

    @staticmethod
    def get_all():
        session = Session()

        users = session.query(User).all()
        user_schema = UserSchema()

        return [user_schema.dumps(user) for user in users]


class CryptoCurrencyService:
    @staticmethod
    def create(name, value):
        crypt = CryptoCurrency(name=name, value=value)
        crypt_scheme = CryptoCurrencySchema()

        session = Session()
        session.add(crypt)
        session.commit()

        return crypt_scheme.dumps(crypt)

    @staticmethod
    def get_all():
        session = Session()

        crypto_currencies = session.query(CryptoCurrency).all()
        crypt_scheme = CryptoCurrencySchema()

        return [crypt_scheme.dumps(crypt) for crypt in crypto_currencies]