import pytest

from app.exceptions import InvalidParams


def test_fetch_all_users(client):
    response = client.get('/users')
    assert response.get_json() == []


def test_create_user(client):
    response = client.post('/users?name=Test')
    assert response.status_code == 200


def test_incorrect_create_user(client):
    with pytest.raises(InvalidParams):
        client.post('/users?age=12')


def test_get_user(client):
    client.post('/users?name=Test')
    user = client.get('/users/1')
    assert user.get_json().get('name') == 'Test'


def test_add_user_crypto(client):
    client.post('/users?name=Test')
    client.post('/crypto-currencies?name=TestCoin&value=12.12')

    client.patch('/users/1/crypto-currencies?crypto_id=1&crypto_count=2')
    client.patch('/users/1/crypto-currencies?crypto_id=1&crypto_count=2')

    user = client.get('/users/1').get_json()

    assert user['wallet']['briefcase'][0]['crypto']['name'] == 'TestCoin'
    assert user['wallet']['briefcase'][0]['crypto']['id'] == 1
    assert user['wallet']['briefcase'][0]['count'] == 4


def test_incorrect_add_user_crypto(client):
    with pytest.raises(InvalidParams):
        client.patch('/users/1/crypto-currencies?cry_id=123123&crypto_count=2')


def test_add_user_crypto_insufficient_funds(client):
    client.post('/users?name=Test')
    client.post('/crypto-currencies?name=TestCoin&value=12.12')

    response = client.patch('/users/1/crypto-currencies?crypto_id=1&crypto_count=10000')

    assert response.data.decode('utf-8') == 'error, insufficient funds'


def test_remove_user_crypto(client):
    client.post('/users?name=Test')
    client.post('/crypto-currencies?name=TestCoin&value=12.12')

    client.patch('/users/1/crypto-currencies?crypto_id=1&crypto_count=10')
    client.delete('/users/1/crypto-currencies?crypto_id=1&crypto_count=9')

    user = client.get('/users/1').get_json()

    assert user['wallet']['briefcase'][0]['crypto']['name'] == 'TestCoin'
    assert user['wallet']['briefcase'][0]['crypto']['id'] == 1
    assert user['wallet']['briefcase'][0]['count'] == 1


def test_incorrect_remove_user_crypto(client):
    with pytest.raises(InvalidParams):
        client.delete('/users/1/crypto-currencies?cry_id=1&crypto_count=9')


def test_remove_user_crypto_insufficient_funds(client):
    client.post('/users?name=Test')
    client.post('/crypto-currencies?name=TestCoin&value=12.12')

    client.patch('/users/1/crypto-currencies?crypto_id=1&crypto_count=10')
    response = client.delete(
        '/users/1/crypto-currencies?crypto_id=1&crypto_count=100000'
    )

    assert response.data.decode('utf-8') == 'error, insufficient funds'


def test_fetch_crypto_currencies(client):
    response = client.get('/crypto-currencies')
    assert response.get_json() == []


def test_create_crypto(client):
    response = client.post('/crypto-currencies?name=Test&value=10.10')
    assert response.status_code == 200


def test_incorrect_create_crypto(client):
    with pytest.raises(InvalidParams):
        client.post('/crypto-currencies?rain=Test&value=10.10')


def test_get_crypto(client):
    client.post('/crypto-currencies?name=Test&value=10.10')
    crypt = client.get('/crypto-currencies/1').get_json()
    assert crypt.get('name') == 'Test'
    assert crypt.get('value') == '10.10'


def test_fetch_transactions(client):
    response = client.get('/transactions')
    assert response.get_json() == []
