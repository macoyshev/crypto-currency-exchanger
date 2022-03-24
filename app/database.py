from contextlib import contextmanager
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm.session import Session as SessionType

DATA_BASE_URL = 'sqlite:///app/rialto.db'
engine = create_engine(DATA_BASE_URL)

DATA_BASE_TEST_URL = 'sqlite:///tests/app/test_rialto.db'
test_engine = create_engine(DATA_BASE_TEST_URL)

Session = sessionmaker()

Base = declarative_base()


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
    Base.metadata.create_all(engine)


def clear_db() -> None:
    Base.metadata.drop_all(engine)


def create_test_db() -> None:
    Session.configure(bind=test_engine)
    Base.metadata.create_all(test_engine)


def clear_test_db() -> None:
    Base.metadata.drop_all(test_engine)
