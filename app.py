from settings import app
from Routes import Article
from threading import Thread

"""
Docu Kram:
sphinx-build -b html source build
Requirement Kram:
pip freeze > requirements.txt
pip install -r requirements.txt
"""


if __name__ == '__main__':
    # with app.app_context():
    #     t = Thread(target=synch, daemon=True)
    #     t.start()

    app.run(host='0.0.0.0')

# todo: amount, haendler, verpackung? many to many insert? Bulk Insert?
