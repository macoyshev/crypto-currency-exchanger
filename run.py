import time
import logging
from threading import Thread

from app import create_app
from app.services import CryptoService


logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")


def emulate_rialto() -> None:
    while True:
        time.sleep(10)
        CryptoService.randomly_change_currency()
        logging.info('a crypto was updated')


app = create_app('DEBUG')
th = Thread(target=emulate_rialto)
th.start()

