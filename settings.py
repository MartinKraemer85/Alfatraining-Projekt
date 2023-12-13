import json

import sqlalchemy as db
from decouple import config

# make the engine available for all modules that need it
from flask import jsonify

engine = db.create_engine(f"mssql://@{config('SERVER')}/{config('DATABASE')}?driver={config('ODBC')}")
current_data = {}


def set_current_data(data):
    global current_data
    current_data = data


def get_current_data():
    global current_data
    return json.dumps(current_data, default=str)
# sqllite fuer Projektabgabe
# engine = db.create_engine(f"sqlite:///project.db", echo=True)
# engine = db.create_engine(f"sqlite:///E:\repos\Plattenfreude\project.db", echo=True)
