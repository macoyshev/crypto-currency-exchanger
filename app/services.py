import random
from decimal import Decimal

from app.database import create_session
from app.exceptions import ZeroWalletBalanceException
from app.models import Crypto, CryptoCounter, User, Wallet


class UserService:
    @staticmethod
    def get_all() -> list[User]:
        with create_session(expire_on_commit=False) as session:
            users = session.query(User).all()

        return users

    @staticmethod
    def get_by_id(user_id: int) -> User:
        with create_session(expire_on_commit=False) as session:
            user = session.query(User).where(User.id == user_id).first()

        return user

    @staticmethod
    def create(name: str) -> None:
        with create_session() as session:
            new_user = User(name=name)
            new_user.wallet = Wallet()

            session.add(new_user)

    @staticmethod
    def add_crypto(user_id: int, crypto_id: int, count: int) -> None:
        with create_session() as session:
            user = session.query(User).where(User.id == user_id).first()
            crypto = session.query(Crypto).where(Crypto.id == crypto_id).first()

            cost = crypto.value * Decimal(count)

            if cost.compare(user.wallet.balance) == Decimal(-1):
                user.wallet.balance -= cost

                # searching for existing crypto in the wallet
                crypto_counter = None
                for cr_counter in user.wallet.briefcase:
                    if cr_counter.crypto.id == crypto_id:
                        crypto_counter = cr_counter

                if not crypto_counter:
                    crypto_counter = CryptoCounter(crypto=crypto, count=count)
                    user.wallet.briefcase.append(crypto_counter)
                else:
                    crypto_counter.count += count

    @staticmethod
    def remove_crypto(user_id: int, crypto_id: int, count: int) -> None:
        with create_session() as session:
            user = session.query(User).where(User.id == user_id).first()
            crypto = session.query(Crypto).where(Crypto.id == crypto_id).first()

            # searching for existing crypto in the wallet
            crypto_counter = None
            for cr_counter in user.wallet.briefcase:
                if cr_counter.crypto.id == crypto_id:
                    crypto_counter = cr_counter

            if crypto_counter and crypto_counter.count >= count:
                crypto_counter.count -= count
                user.wallet.balance += crypto.value * Decimal(count)

                if crypto_counter.count == 0:
                    session.delete(crypto_counter)
            else:
                raise ZeroWalletBalanceException()


class CryptoService:
    @staticmethod
    def get_all() -> list[Crypto]:
        with create_session(expire_on_commit=False) as session:
            crypts = session.query(Crypto).all()

        return crypts

    @staticmethod
    def get_by_id(crypto_id: int) -> Crypto:
        with create_session(expire_on_commit=False) as session:
            crypt = session.query(Crypto).filter(Crypto.id == crypto_id).first()

        return crypt

    @staticmethod
    def create(name: str, value: str) -> None:
        with create_session() as session:
            crypt = Crypto(name=name, value=value)
            session.add(crypt)

    @staticmethod
    def randomly_change_currency() -> None:
        crypts = CryptoService.get_all()

        crypto = random.choice(crypts)
        new_val = (
            Decimal(crypto.value) * Decimal(random.randint(90, 110)) / Decimal(100)
        )

        with create_session() as session:
            crypto_to_update = (
                session.query(Crypto).where(Crypto.id == crypto.id).first()
            )
            crypto_to_update.value = new_val
