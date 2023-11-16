from flask import Flask
from Routes.Article import article
from Routes.Mail import mail
from Routes.HelloWorld import hello_world
from flask_cors import CORS
from config_ import engine

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
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0')

# fastapi