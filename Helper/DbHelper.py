import json
from dataclasses import dataclass
import pyodbc
from decouple import config

from Helper.GeneralHelper import generate_classinstance
from Model.ModelBase import ModelBase

@dataclass()
class DbHelper:
    """
    This class holds all the needed functions to query the database.

    """
    cursor: any = None

    def __init__(self):
        self.cursor = pyodbc.connect(driver=config("DRIVER"),
                                     server=config("SERVER"),
                                     database=config("DATABASE"),
                                     user=config("USER"),
                                     password=config("PWD"),
                                     trusted_connection='yes').cursor()

    def __del__(self):
        self.cursor.close()

    def select(self, table_name: str, columns: list, where: str = "") -> str:
        """
        Returns the rows for a query in a dictionary string.

        :param table_name: Table to query
        :param columns: columns to query
        :param where: where condition if needed
        :return: None
        """
        query = f'SELECT {",".join(columns)} FROM {table_name} {where};'
        ret = [dict(zip(columns, row)) for row in self.cursor.execute(query).fetchall()]
        return json.dumps(ret, indent=2)

    def insert(self, values: dict) -> None:
        """
        Insert values into the db

        :param values: dict that reflects the object
        :return: None
        """
        values = {"objectType": "Model.Vinyl.Record.Record",
                  "object":
                      {"title": "test", "artist": "cameltoe",
                       "Model.Vinyl.Track.Track": [
                           {"title": "schnupp", "length": "5:23"},
                           {"title": "schnarr", "length": "4:23"}
                       ]},
                  }

        print(generate_classinstance(values.get("objectType"), values))
        return None

