class RequestException(Exception):
    pass


class InvalidParams(RequestException):
    pass


class ZeroWalletBalanceException(Exception):
    pass
