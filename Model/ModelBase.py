from dataclasses import dataclass, field, asdict
from typing import List
from sqlalchemy import Column, Integer, String, Boolean, Numeric, Time, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from Helper.GeneralHelper import generate_classinstance


class Base(DeclarativeBase):
    """
    | Declarative base for mapped classes.
    | https://docs.sqlalchemy.org/en/20/tutorial/metadata.html#using-orm-declarative-forms-to-define-table-metadata

    """
    pass


@dataclass()
class ModelBase():
    # TODO: Tu es!

    def set_properties(self, properties: dict) -> None:
        """
        | Set the properties of an instance via dictionary.
        | As Example a Record dictionary:
        | {"objectType": "Model.Vinyl.Record.Record",
        |           "object":
        |               {"title": "test", "artist": "cameltoe",
        |                "Model.Vinyl.Track.Track": [
        |                    {"name": "schnupp", "length": "5:23"},
        |                    {"name": "schnarr", "length": "4:23"}
        |                ]},
        |           }+

        :param properties: Dictionary of properties
        :return: None
        """
        pass
