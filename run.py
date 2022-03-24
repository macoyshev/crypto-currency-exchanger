import threading

from app import create_app
from app.services import emulate_rialto, CryptoService
from app.database import create_db


app = create_app()
create_db()

th2 = threading.Thread(target=emulate_rialto)
th2.start()
