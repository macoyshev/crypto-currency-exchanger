from app.database import create_session
from app.models import CryptoCurrency, User, Wallet


class UserService:
    @staticmethod
    def get_all() -> list[User]:
        with create_session(expire_on_commit=False) as session:
            users = session.query(User).all()

        return users

    @staticmethod
    def create(name: str) -> None:
        with create_session() as session:
            new_user = User(name=name)
            new_user.wallet = Wallet()

            session.add(new_user)

    # TODO: реализовать покукку крипты
    # @staticmethod
    # def buy_crypts(user_id: int, crypto_id: int, count: int) -> None:
    #     with create_session() as session:
    #         user = session.query(User).filter(User.id == user_id)


class CryptoCurrencyService:
    @staticmethod
    def get_all() -> list[CryptoCurrency]:
        with create_session(expire_on_commit=False) as session:
            crypts = session.query(CryptoCurrency).all()

        return crypts

    @staticmethod
    def create(name: str, value: float) -> None:
        with create_session() as session:
            crypt = CryptoCurrency(name=name, value=value)
            session.add(crypt)

    @staticmethod
    def get_by_id(crypto_id: int) -> CryptoCurrency:
        with create_session() as session:
            crypt = session.query(CryptoCurrency).filter(CryptoCurrency.id == crypto_id)

        return crypt
