# currency_exchange

### Description:
API for cryptocurrency exchanges.
You can get acquainted with all existing crypto-currencies
by making requests on `/crypto-currencies`. 
Every 10 seconds currency rate changes, take it into account.
To take part in trading, create a user for this make 
`post` request on `/users` 
with param name as in the example 
`/users?name=Tom`. After that, you can get access to 
the account using id `/users/{id}`. To buy crypto,
make a `patch` request on 
`/users/{id}/crypto-currencies` with params 
crypto_id and crypto_count, as in the example 
`/users/1/crypto-currencies?crypto_id=1&crypto_count=2`, 
to sell a crypto make `delete` request 
on `/users/{id}/crypto-currencies` with 
crypto_id and crypto_count respectively. Also, you can 
create your crypto-currency, make a `post` request
on `/crypto-currencies` with params name and value of new crypto `/crypto-currencies?name=BitCoin&value=12.12`.
To see transactions, follow `/transactions`
. `ctrl + C` to exit from the app

### Create venv:
    make venv

### Run tests:
    make test

### Run application
    make run

### Run debug
    make debug
_Note: if you want to check the capability of the application, please use command_ __"make run"__, _because
in debug mode Flask triggers threads 2 times, and crypto-currency changes 2 times as well. This does not 
affect on work of the application critically, but you should take it into account._

### Run linters:
    make lint

### Run formatters:
    make format