import pytest

from app import create_app


@pytest.fixture
def client():
    app = create_app('TESTING')
    app.config.update(
        {
            'TESTING': True,
        }
    )

    yield app.test_client()
