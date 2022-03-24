import random
import sys
import time
from decimal import Decimal

from loguru import logger

from app.database import create_session
from app.exceptions import InsufficientFunds
from app.models import Crypto, CryptoCounter, Transaction, User, Wallet

logger.remove()
logger.add(
    sys.stdout,
    level='INFO',
    format='<blue>{time:hh:mm:ss.SS} | {level} | {message}</blue>',
    colorize=True,
)


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

            logger.info(f'{name} was added')

    @staticmethod
    def buy_crypto(user_id: int, crypto_id: int, count: int) -> None:
        with create_session() as session:
            user = session.query(User).where(User.id == user_id).first()
            crypto = session.query(Crypto).where(Crypto.id == crypto_id).first()

            cost = Decimal(crypto.value) * Decimal(count)

            if cost.compare(Decimal(user.wallet.balance)) == Decimal(-1):
                user.wallet.balance = str(Decimal(user.wallet.balance) - cost)

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

                TransactionService.record(
                    status='success',
                    wallet_id=user.wallet.id,
                    description=f'user id:{user_id} bought {count} crypto id:{crypto_id}',
                )

            else:
                TransactionService.record(
                    status='error',
                    wallet_id=user.wallet.id,
                    description=f'user id:{user_id} failed to buy {count} crypto id:{crypto_id}',
                )

                raise InsufficientFunds()

    @staticmethod
    def sell_crypto(user_id: int, crypto_id: int, count: int) -> None:
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
                user.wallet.balance = str(
                    Decimal(user.wallet.balance)
                    + Decimal(crypto.value) * Decimal(count)
                )

                if crypto_counter.count == 0:
                    session.delete(crypto_counter)

                TransactionService.record(
                    status='Error',
                    description=f'user id:{user_id} sold {count} crypto id:{crypto_id}',
                    wallet_id=user.wallet.id,
                )
            else:
                raise InsufficientFunds()


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

            logger.info(f'{name} was added')

    @staticmethod
    def randomly_change_currency() -> None:
        crypts = CryptoService.get_all()

        if len(crypts) != 0:
            crypto = random.choice(crypts)
            new_val = str(
                Decimal(crypto.value) * Decimal(random.randint(90, 110)) / Decimal(100)
            )

            with create_session() as session:
                crypto_to_update = (
                    session.query(Crypto).where(Crypto.id == crypto.id).first()
                )
                crypto_to_update.value = new_val

                logger.info('rialto was updated')


class TransactionService:
    @staticmethod
    def get_all() -> list[Transaction]:
        with create_session(expire_on_commit=False) as session:
            transactions = session.query(Transaction).all()

        return transactions

    @staticmethod
    def record(status: str, description: str, wallet_id: int) -> None:
        with create_session() as session:
            transaction = Transaction(
                description=description, status=status, wallet_id=wallet_id
            )
            session.add(transaction)

            logger.info(f'transaction: {description}')


def emulate_rialto() -> None:
    while True:
        time.sleep(10)
        CryptoService.randomly_change_currency()
