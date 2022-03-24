from contextlib import contextmanager
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm.session import Session as SessionType

DATA_BASE_URL = 'sqlite:///./primary.db'
DATA_BASE_TEST_URL = 'sqlite:///test/app/test.db'

Base = declarative_base()

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
    engine = create_engine(DATA_BASE_URL)

    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
