import threading

from app import create_app
from app.services import emulate_rialto


app = create_app()

th2 = threading.Thread(target=emulate_rialto)
th2.start()
