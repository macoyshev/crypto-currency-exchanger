from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATA_BASE_URL = 'sqlite:///./primary.db'
DATA_BASE_TEST_URL = 'sqlite:///test/app/test.db'

Base = declarative_base()

Session = sessionmaker()


def create_db(mode: str) -> None:
    if mode == 'TESTING':
        engine = create_engine(DATA_BASE_TEST_URL, echo=True)
    else:
        engine = create_engine(DATA_BASE_URL, echo=True)

    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
