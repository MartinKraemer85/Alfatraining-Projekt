from flask import Flask
from Routes.Article import article

app = Flask(__name__)
app.register_blueprint(article)

# sphinx-build -b html source build
# pip freeze > requirements.txt

# from Model.Vinyl.Record import *
# record = Record(title="Schnarr", artist="Muh")
# record.add_track(Track(title="Niau", length=time(minute=5, second=23)))

if __name__ == '__main__':
    app.run(host='0.0.0.0')

# TODO: Superclass anlegen