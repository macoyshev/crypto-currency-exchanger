
from sqlalchemy import DECIMAL, Column, Integer, String

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class UserSchema():




class CryptoCurrency(Base):
    __tablename__ = 'crypto-currencies'

    id = Column(Integer, primary_key=True)
    name = Column(String(30), unique=True, nullable=False)
    value = Column(DECIMAL(19, 4), nullable=False)

    def __repr__(self):
        return f'<Crypto {self.name} : {self.value}>'

    def as_dict(self):
        return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}
