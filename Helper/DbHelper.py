import json
from dataclasses import dataclass
import pyodbc
from decouple import config


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

    def select(self, table_name: str, where: str, columns: list) -> str:
        """
        Returns the rows for a query in a list.

        :param table_name: Table to query
        :param where: where condition if needed
        :param columns: columns to query
        :return:
        """
        query = f'SELECT {",".join(columns)} FROM {table_name} {where};'
        ret = [dict(zip(columns, row)) for row in self.cursor.execute(query).fetchall()]
        return json.dumps(ret, indent=2)
