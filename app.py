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

import pyodbc
#sal.create_engine(‘dialect+driver://username:password@host:port/database’)
# https://medium.com/@anushkamehra16/connecting-to-sql-database-using-sqlalchemy-in-python-2be2cf883f85
# print(f"mssql+pyodbc://{config('USER')}:{config('PWD')}@{config('SERVER')}:{config('PORT')}/{config('DATABASE')}?driver=SQL+Server")
# parsing the url, so spaces i.e. will be replaced with +
# params = urllib.parse.quote_plus(f"DRIVER={config('ODBC')};SERVER=\'{config('SERVER')}\';DATABASE=\'{config('DATABASE')}\';UID=\'{config('USER')}\';PWD=\'{config('PWD')}\'")

print(f"mssql://@{config('SERVER')}/{config('DATABASE')}?driver={config('ODBC')}")
engine = db.create_engine(f"mssql://@{config('SERVER')}/{config('DATABASE')}?driver={config('ODBC')}")
connection = engine.connect()
metadata = db.MetaData()
test = db.Table("record", metadata, autoload_with=engine)
query = db.select([test])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
print(ResultSet)
# sql_query = pd.read_sql_query(‘SELECT * FROM database_name.dbo.tablename’, engine)
# with engine.connect() as conn:
#     engine.ex
