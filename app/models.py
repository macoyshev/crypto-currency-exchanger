from dataclasses import dataclass

from sqlalchemy import DECIMAL, Column, Integer, String

from app.database import Base


@dataclass
class User(Base):
    __tablename__ = 'users'

    name: str

    id: int = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)


@dataclass()
class CryptoCurrency(Base):
    __tablename__ = 'crypto-currencies'

    value: float
    name: str

    id: int = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    value = Column(DECIMAL(19, 4), nullable=False)
