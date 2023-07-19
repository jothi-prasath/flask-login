from app import app
import os
from config import HOST, PORT

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(host=HOST, port=PORT)