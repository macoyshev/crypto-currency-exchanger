from app.models import User, CryptoCurrency, db


class UserService:
    @staticmethod
    def get_all():
        users = User.query.all()

        return users

    @staticmethod
    def create(name):
        user = User(name=name)

        db.session.add(user)
        db.session.commit()

        return user


class CryptoCurrencyService:
    @staticmethod
    def create(name: str, value: float):
        crypt = CryptoCurrency(name=name, value=value)

        db.session.add(crypt)
        db.session.commit()

        return crypt

    @staticmethod
    def get_all() -> list[str]:
        crypt_currencies = CryptoCurrency.query.all()

        return crypt_currencies
