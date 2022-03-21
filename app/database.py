from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


DATA_BASE_URL = 'sqlite:///./test.db'

engine = create_engine(DATA_BASE_URL)

Session = sessionmaker(engine)

Base = declarative_base()
