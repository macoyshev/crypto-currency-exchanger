from marshmallow import Schema
from sqlalchemy import DECIMAL, Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<User {self.username}>'


class UserSchema(Schema):
    class Meta:
        fields = ('id', 'username')


class CryptoCurrency(Base):
    __tablename__ = 'crypto-currencies'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    value = Column(DECIMAL(19, 4), nullable=False)

    def __repr__(self) -> str:
        return f'<Crypto {self.name} : {self.value}>'


class CryptoCurrencySchema(Schema):
    class Meta:
        fields = ('id', 'name', 'value')
