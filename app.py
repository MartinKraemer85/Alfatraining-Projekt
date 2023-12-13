import time
from flask import Flask
from Routes.Article import article
from Routes.Mail import mail
from Routes.HelloWorld import hello_world
from flask_cors import CORS
from Services.Synchronize import synch
from settings import engine

app = Flask(__name__)
CORS(app)

app.register_blueprint(article)
app.register_blueprint(mail)
app.register_blueprint(hello_world)

"""
Docu Kram:
sphinx-build -b html source build
Requirement Kram:
pip freeze > requirements.txt
pip install -r requirements.txt
"""

from threading import Thread

if __name__ == '__main__':
    with app.app_context():
        t = Thread(target=synch, daemon=True)
        t.start()

    app.run(host='0.0.0.0')

# todo: amount, haendler, verpackung? many to many insert? Bulk Insert?
