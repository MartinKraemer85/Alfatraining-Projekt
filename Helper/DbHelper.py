from dataclasses import dataclass

from flask import jsonify, Response
from sqlalchemy import Engine, text, Connection, update, Table, MetaData, select
from sqlalchemy.exc import ProgrammingError, InternalError, DataError, IntegrityError, ArgumentError
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import UnmappedInstanceError
from Helper.GeneralHelper import generate_classinstance, get_class


@dataclass()
class DbHelper:
    """
    This class holds all the needed functions to query the database.

    """
    engine: Engine
    __conn: Connection = None
    __metadata_obj = MetaData()

    def select(self, table_name: str, columns: list, where: str = "") -> list[dict]:
        """
        Returns the rows for a query in a dictionary string.

        :param table_name: Table to query
        :param columns: columns to query
        :param where: where condition if needed
        :return: The result as a list of dictionary's
        """
        query = f'SELECT {"*" if "*" in columns else ",".join(columns)} FROM {table_name} {where};'
        conn = self.engine.connect()
        result = conn.execute(text(query))
        return [dict(zip(result.keys(), row)) for row in result.fetchall()]

    def select_all(self, object_path: str, initial: True) -> Response:
        """
        Select all rows + relationships of a table.

        :param object_path: The object we want to select (i.e. "Model.Vinyl.Record.Record")
        :param initial: for the initial select, limit to 50 (?)
        :return: object of the given path
        """
        res = []
        select_obj = get_class(object_path)
        with Session(self.engine) as session:
            session.expire_on_commit = False
            if initial:
                result = session.execute(select(select_obj).limit(50)).unique()
            else:
                result = session.execute(select(select_obj)).unique()

            for row in result.scalars().all():
                res.append(row.to_dict())
        return res

        select_obj = get_class(object_path)
        # select_ = select(select_obj).limit(10).offset(pageSize*page)
        with Session(self.engine) as session:
            if initial:
                result = session.execute(select(select_obj).limit(1)).unique()
            else:
                result = session.execute(select(select_obj).limit(1)).unique()

            return result.scalars().all()

    def db_update(self, values: dict) -> int:
        """
        | Perform an update with a dictionary that holds the list of changes.
        | I.e.:
        | {"objectPath": "Model.Vinyl.Record.Record",
        |        "attributes": [
        |            {"id": "13", "title": "updat1", "artist": "asddds"},
        |            {"id": "14", "title": "updat2456", "artist": "schnurr"}
        |        ]})

        :param values: Update dictionary
        :return: 1 - success
                 2 - ProgrammingError
                 3 - InternalError
                 4 - DataError
                 5 - UnmappedInstanceError
                 6 - IntegrityError
                 7 - ArgumentError
        """
        # todo: errorhandling
        with Session(self.engine) as session:
            try:
                session.execute(
                    update(get_class(values.get("objectPath"))),
                    values.get("attributes")
                )
                session.flush()
                session.commit()
            except ProgrammingError:
                return 2
            except InternalError:
                return 3
            except DataError:
                return 4
            except UnmappedInstanceError:
                return 5
            except IntegrityError:
                return 6
            except ArgumentError:
                return 7

        return 1

    def db_insert(self, values: dict) -> int:
        """
        | Insert a new row with the given dictionary. I.e.:
        | {"objectType": "Model.Vinyl.Record.Record",
        |           "object":
        |               {"title": "test", "artist": "cameltoe",
        |                "Model.Vinyl.Track.Track": [
        |                    {"name": "schnupp", "length": "5:23"},
        |                    {"name": "schnarr", "length": "4:23"}
        |                ]},
        |           }

        :param values: dict that reflects the object
        :return: 1 - success
                 2 - ProgrammingError
                 3 - InternalError
                 4 - DataError
                 5 - UnmappedInstanceError
                 6 - IntegrityError
                 7 - ArgumentError
        """

        insert_obj = generate_classinstance(values.get("objectPath"), values)

        with Session(self.engine) as session:
            session.add(insert_obj)
            session.flush()
            session.commit()
            try:
                session.add(insert_obj)
                session.flush()
                session.commit()
                return 1
            except ProgrammingError:
                return 2
            except InternalError:
                return 3
            except DataError:
                return 4
            except UnmappedInstanceError:
                return 5
            except IntegrityError:
                return 6
            except ArgumentError:
                return 7

    def delete(self, values: dict) -> int:
        """
        | Delete record(s) by id.
        | I.e.:
        | {"objectPath": "Model.Vinyl.Record.Record",
        |     "ids": [20, 21, 19]}

        :param values: Dictionary with table object and list to delete
        :return: 1 - success
                 2 - ProgrammingError
                 3 - InternalError
                 4 - DataError
                 5 - UnmappedInstanceError
                 6 - IntegrityError
                 7 - ArgumentError
        """
        with Session(self.engine) as session:
            try:
                delete_obj = get_class(values.get("objectPath"))
                for id_ in values.get("ids"):
                    to_delete = session.scalars(select(delete_obj).filter_by(id=id_)).first()
                    # make sure the element exists
                    if to_delete:
                        session.delete(to_delete)
                session.commit()
                return 1
            except ProgrammingError:
                return 2
            except InternalError:
                return 3
            except DataError:
                return 4
            except UnmappedInstanceError:
                return 5
            except IntegrityError:
                return 6
            except ArgumentError:
                return 7
