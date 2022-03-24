import os
import threading

from app import create_app
from app.services import emulate_rialto, CryptoService
from app.database import create_db


app = create_app()
create_db()

if not CryptoService.get_all():
    CryptoService.create(name='BitCoin', value='300')
    CryptoService.create(name='ETH', value='10')
    CryptoService.create(name='BatmanCoin', value='5.5')
    CryptoService.create(name='MegaMind', value='111')
    CryptoService.create(name='Splinter', value='1000000')

th2 = threading.Thread(target=emulate_rialto)
th2.start()
