from dataclasses import dataclass, field, asdict
from typing import List
from datetime import time
from sqlalchemy import Column, Integer, String, Boolean, Numeric, Time, ForeignKey,Table
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from Helper.GeneralHelper import generate_classinstance


class Base(DeclarativeBase):
    """
    | Declarative base for mapped classes.
    | https://docs.sqlalchemy.org/en/20/tutorial/metadata.html#using-orm-declarative-forms-to-define-table-metadata

    """
    pass


@dataclass()
class ModelBase:

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
        |           }

        :param properties: Dictionary of properties
        :return: None
        """
        for key, value in properties.get("attributes").items():
            print(key, value)
            setattr(self, key, value)
