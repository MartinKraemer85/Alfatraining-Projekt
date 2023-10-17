import json
from dataclasses import dataclass
import pyodbc
from decouple import config
from Helper.GeneralHelper import generate_classinstance

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
                                     trusted_connection='yes').cursor()

    def __del__(self):
        self.cursor.close()

    def select(self, table_name: str, columns: list, where="") -> str:
        """
        Returns the rows for a query in a dictionary string.

        :param table_name: Table to query
        :param columns: columns to query
        :param where: where condition if needed
        :return:
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
        values = {"objectType": "Record",
                  "object":
                      {"title": "test", "artist": "cameltoe",
                       "tracks": [
                           {"title": "schnupp", "length": "5:23"},
                           {"title": "schnarr", "length": "4:23"}
                       ]},
                  }

        print(generate_classinstance("Record", values))
