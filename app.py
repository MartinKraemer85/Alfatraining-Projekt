from flask import Flask
from sqlalchemy.orm import Session

from Model.Vinyl.Record import Record
from Routes.Article import article
from Routes.mail import mail
from decouple import config
import sqlalchemy as db

app = Flask(__name__)

app.register_blueprint(article)
app.register_blueprint(mail)

"""
Docu Kram:
sphinx-build -b html source build
Requirement Kram:
pip freeze > requirements.txt
"""

engine = db.create_engine(f"mssql://@{config('SERVER')}/{config('DATABASE')}?driver={config('ODBC')}")

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')

#---- testing stuff ------------
from Helper.DbHelper import DbHelper
test = DbHelper(engine)

# test.db_update({"objectPath": "Model.Vinyl.Record.Record",
#                 "attributes": [
#                     {"id": "13", "title": "updat1", "artist": "addd"},
#                     {"id": "14", "title": "updat2456", "artist": "schnurr"}
#                 ]})


test.db_insert({"objectPath": "Model.Vinyl.Record.Record",
                "attributes":
                    {"title": "asfdgfsd", "artist": "asd",
                     "Model.Vinyl.Track.Track": [
                         {"name": "track1", "length": "5:23"},
                         {"name": "track2", "length": "5:23"},
                         {"name": "track3", "length": "5:23"},
                     ]},
                })

# print(test.delete({"objectPath": "Model.Vinyl.Record.Record",
#                    "ids": [i for i in range(20, 100)]}))
