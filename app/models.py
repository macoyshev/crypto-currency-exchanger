from dataclasses import dataclass

from sqlalchemy import DECIMAL, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


@dataclass()
class CryptoCurrency(Base):
    __tablename__ = 'crypto-currencies'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(30), unique=True, nullable=False)
    value: float = Column(DECIMAL(19, 4), nullable=False)
    wallet_id: int = Column(Integer, ForeignKey('wallets.id'))

    wallet = relationship(
        'Wallet', back_populates='crypts', uselist=False, lazy='subquery'
    )


@dataclass
class Wallet(Base):
    __tablename__ = 'wallets'

    id: int = Column(Integer, primary_key=True)
    budget: int = Column(Integer, default=1000)

    user = relationship('User', back_populates='wallet', uselist=False)
    crypts: CryptoCurrency = relationship(
        CryptoCurrency, back_populates='wallet', uselist=True, lazy='subquery'
    )


@dataclass
class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(30), unique=True, nullable=False)
    wallet_id: int = Column(Integer, ForeignKey(Wallet.id), nullable=False)

    wallet: Wallet = relationship(
        Wallet, back_populates='user', uselist=False, lazy='subquery'
    )
