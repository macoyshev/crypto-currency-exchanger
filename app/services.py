from app.models import User, CryptoCurrency
from app.database import Session


class UserService:
    @staticmethod
    def get_all() -> list[User]:
        session = Session()
        users = session.query(User).all()

        return users

    @staticmethod
    def create(name: str) -> User:
        user = User(name=name)

        session = Session()
        session.add(user)
        session.commit()
        session.refresh(user)

        return user


class CryptoCurrencyService:
    @staticmethod
    def get_all() -> list[CryptoCurrency]:
        session = Session()
        crypt_currencies = session.query(CryptoCurrency).all()

        return crypt_currencies


    @staticmethod
    def create(name: str, value: float) -> CryptoCurrency:
        crypt = CryptoCurrency(name=name, value=value)

        session = Session()
        session.add(crypt)
        session.commit()
        session.refresh(crypt)

        return crypt

    @staticmethod
    def get_by_id(crypto_id: int) -> CryptoCurrency:
        session = Session()
        return session.query(CryptoCurrency).filter(CryptoCurrency.id == crypto_id)

    @staticmethod
    def update(crypt: CryptoCurrency):
        crypt_to_change = CryptoCurrencyService.get_by_id(crypt.id)

        # TODO: make update query https://docs.sqlalchemy.org/en/14/tutorial/orm_data_manipulation.html

