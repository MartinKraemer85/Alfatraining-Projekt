import math
import urllib
from flask import Flask
from Routes.Article import article
from Routes.mail import mail
from decouple import config

app = Flask(__name__)

app.register_blueprint(article)
app.register_blueprint(mail)

"""
Docu Kram:
sphinx-build -b html source build
Requirement Kram:
pip freeze > requirements.txt
"""

# from Helper.DbHelper import DbHelper
# dbhelper = DbHelper()
# dbhelper.insert({})
# print(dbhelper.select("record", "*"))
# record = Record(title="Schnarr", artist="Muh")
# record.add_track(Track(title="Niau", length=time(minute=5, second=23)))

# if __name__ == '__main__':
#     app.run(host='0.0.0.0')

# TODO: Superclass anlegen

import sqlalchemy as db
from Model.Vinyl.Record import Record
from sqlalchemy import select
from sqlalchemy.orm import Session

engine = db.create_engine(f"mssql://@{config('SERVER')}/{config('DATABASE')}?driver={config('ODBC')}")
connection = engine.connect()

session = Session(engine)

stmt = select(Record).where(Record.title.in_(["test", "test2"]))
# print(stmt)
for record in session.scalars(stmt):
    print(record)
#
# with engine.connect() as conn:
#     conn.execute(stmt)


def faku(n):
    return n * faku(n - 1) if n > 1 else 1
#
#
print(faku(6))
