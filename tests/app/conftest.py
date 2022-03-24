import pytest

from app import create_app
from app.database import clear_test_db, create_test_db


@pytest.fixture
def client():
    app = create_app()
    app.config.update(
        {
            'TESTING': True,
        }
    )
    yield app.test_client()


@pytest.fixture(autouse=True)
def _init_db():
    create_test_db()
    yield
    clear_test_db()
