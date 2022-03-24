import os
from contextlib import contextmanager
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session as SessionType

from app import models

DATA_BASE_URL = 'sqlite:///app/rialto.db'
engine = create_engine(DATA_BASE_URL)

DATA_BASE_TEST_URL = 'sqlite:///tests/app/test_rialto.db'
test_engine = create_engine(DATA_BASE_TEST_URL)

Session = sessionmaker()


@contextmanager
def create_session(**kwargs: Any) -> SessionType:
    new_session = Session(**kwargs)
    try:
        yield new_session
        new_session.commit()
    except Exception:
        new_session.rollback()
        raise
    finally:
        new_session.close()


def create_db() -> None:
    Session.configure(bind=engine)
    models.Base.metadata.create_all(engine)

    if not os.path.exists('app/rialto.db'):
        with create_session() as session:
            session.add(models.Crypto(name='BitCoin', value='300'))
            session.add(models.Crypto(name='ETH', value='10'))
            session.add(models.Crypto(name='BatmanCoin', value='5.5'))
            session.add(models.Crypto(name='MegaMind', value='111'))
            session.add(models.Crypto(name='Splinter', value='1000000'))


def clear_db() -> None:
    models.Base.metadata.drop_all(engine)


def create_test_db() -> None:
    Session.configure(bind=test_engine)
    models.Base.metadata.create_all(test_engine)


def clear_test_db() -> None:
    models.Base.metadata.drop_all(test_engine)
