from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, update, MetaData, select
from sqlalchemy.exc import ProgrammingError, InternalError, DataError, IntegrityError, ArgumentError
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import UnmappedInstanceError
from Helper.GeneralHelper import generate_classinstance, get_class


@dataclass()
class DbHelper:
    """
    This class holds all the needed functions to query the database.

    """
    db: SQLAlchemy
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

        result = self.db.session.execute(text(query))
        return [dict(zip(result.keys(), row)) for row in result.fetchall()]

    def select_all_where(self, object_path: str, where: "") -> list:
        """
        Select all rows + relationships of a table.

        :param object_path: The object we want to select (i.e. "Model.Vinyl.Record.Record")
        :param where: The where clause
        :return: object of the given path
        """
        select_obj = get_class(object_path)
        if where:
            result = self.db.session.query(select_obj).filter(text(where))
        else:
            result = self.db.session.query(select_obj)

        return [row.to_dict() for row in result]

    def update(self, object_path: str, values: dict) -> int:
        """
        | Perform an update with a dictionary that holds the list of changes.
        | I.e.:
        | {"objectPath": "Model.Vinyl.Record.Record",
        |        "attributes": [
        |            {"id": "13", "title": "updat1", "artist": "asddds"},
        |            {"id": "14", "title": "updat2456", "artist": "schnurr"}
        |        ]})

        :param object_path:
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
        select_obj = get_class(object_path)

        self.db.session.execute(
            update(select_obj),
            [
                values
            ]
        )
        self.db.session.flush()
        self.db.session.commit()

        return 1

    def db_insert(self, values: dict) -> int:
        """
        | Insert a new row with the given dictionary. I.e.:
        |
        | {"objectPath": "Model.CustomerDetails.Customer.Customer",
        |                 "attributes": {"username": "test",
        |                                "pwd": "miau",
        |                                "first_name": "miau",
        |                                "last_name": "schnarr",
        |                                "mail": "mail@bla.de"},
        | }

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
        try:
            self.db.session.add(insert_obj)
            self.db.session.flush()
            self.db.session.commit()
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
        with Session(self.db) as session:
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
