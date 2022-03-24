import time
import threading
from multiprocessing import Process

from app import create_app
from app.services import CryptoService


def emulate_rialto() -> None:
    while True:
        time.sleep(10)
        CryptoService.randomly_change_currency()


if __name__ == '__main__':
    rialto = Process(target=emulate_rialto)
    rialto.daemon = True
    rialto.start()

    app = create_app('DEBUG')
