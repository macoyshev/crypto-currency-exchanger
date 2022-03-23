from dataclasses import dataclass

from sqlalchemy import DECIMAL, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

    # crypts = relationship('CryptoCurrency')


@dataclass()
class CryptoCurrency(Base):
    __tablename__ = 'crypto-currencies'

    value: float
    name: str

    id: int = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    value = Column(DECIMAL(19, 4), nullable=False)
    wallet_id = Column(Integer, ForeignKey('wallet.id'))

@dataclass
class Wallet(Base):
    __tablename__ = 'wallet'

    id: int = Column(Integer, primary_key=True)
    budget: int = Column(Integer, default=1000)
    user_id = Column(Integer, ForeignKey('users.id'))

    crypts = relationship('CryptoCurrency')

@dataclass
class User(Base):
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(30), unique=True, nullable=False)
    wallets: Wallet = relationship('Wallet')
