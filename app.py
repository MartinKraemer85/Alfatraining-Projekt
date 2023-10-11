from flask import Flask

from Model.Vinyl.Record import *
from Routes.Article import article

app = Flask(__name__)
app.register_blueprint(article)


record = Record(title="Schnarr", artist="Muh")
record.add_track(Track(title="Niau", length=time(minute=5, second=23)))

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')
