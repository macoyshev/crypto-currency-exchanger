from app.database import Session
from app.models import CryptoCurrency, User, Wallet


class UserService:
    @staticmethod
    def get_all() -> list[User]:
        session = Session()
        users = session.query(User).all()

        return users

    @staticmethod
    def create(name: str) -> User:
        wallet = Wallet()
        user = User(name=name)
        user.wallets.append(wallet)

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
    def update(crypt: CryptoCurrency) -> None:
        session = Session()

        session.query(CryptoCurrency).filter(CryptoCurrency.id == crypt.id).update(
            {CryptoCurrency.name: crypt.name}
        )
