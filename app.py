from flask import Flask
from Routes.Article import article
from Routes.Mail import mail


app = Flask(__name__)

app.register_blueprint(article)
app.register_blueprint(mail)

"""
Docu Kram:
sphinx-build -b html source build
Requirement Kram:
pip freeze > requirements.txt
"""

if __name__ == '__main__':
    app.run(host='0.0.0.0')

