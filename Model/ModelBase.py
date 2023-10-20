from dataclasses import dataclass, field, asdict
from sqlalchemy import Column, Integer, String, Boolean, Numeric, Time, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from Helper.GeneralHelper import generate_classinstance


Base = declarative_base()

@dataclass()
class ModelBase():
    # TODO: Tu es!

    def set_properties(self, properties: dict) -> None:
        """
        Set the properties of an instance via dictionary

        :param properties: Dictionary of properties
        :return: None
        """
        pass
