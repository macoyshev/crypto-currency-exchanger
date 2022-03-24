import time
import logging
import threading

from app import create_app
from app.services import CryptoService


def emulate_rialto() -> None:
    while True:
        time.sleep(10)
        CryptoService.randomly_change_currency()
        logging.info('rialto was updated')


app = create_app('DEBUG')

rialto = threading.Thread(target=emulate_rialto)
rialto.setDaemon(True)
rialto.start()

