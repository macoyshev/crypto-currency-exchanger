class RequestException(Exception):
    pass


class InvalidParams(RequestException):
    pass


class InsufficientFunds(Exception):
    pass
