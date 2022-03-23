from dataclasses import dataclass

from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship

from app.database import Base


@dataclass()
class Crypto(Base):
    __tablename__ = 'crypto_currencies'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(30), unique=True, nullable=False)
    value: Numeric = Column(Numeric(19, 4), nullable=False)

    crypto_counter_id = Column(Integer, ForeignKey('crypto_counters.id'))


@dataclass
class CryptoCounter(Base):
    __tablename__ = 'crypto_counters'

    id: int = Column(Integer, primary_key=True)
    count: int = Column(Integer, default=0)

    wallet_id = Column(Integer, ForeignKey('wallets.id'))
    crypto: Crypto = relationship(
        Crypto,
        lazy='subquery',
        uselist=False,
    )


@dataclass
class Wallet(Base):
    __tablename__ = 'wallets'

    id: int = Column(Integer, primary_key=True)
    balance: Numeric = Column(Numeric(19, 4), default=1000)

    user_id = Column(Integer, ForeignKey('users.id'))

    crypto_currency_counters: CryptoCounter = relationship(
        CryptoCounter, uselist=True, lazy='subquery'
    )


@dataclass
class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(30), unique=True, nullable=False)

    wallet: Wallet = relationship(Wallet, uselist=False, lazy='subquery')
