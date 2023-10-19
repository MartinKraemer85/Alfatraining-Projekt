from datetime import time

from Model.ModelBase import *


@dataclass()
class Track(ModelBase):
    """
    A class that holds the Article properties

    """
    # title of the vinyl record
    title: str = None
    # the artist of the vinyl record
    length: time = None

    def set_properties(self, properties: dict) -> None:
        """


        :param properties:
        :return:
        """
        for key, value in properties.items():
            setattr(self, key, value)

    def dict(self) -> dict:
        """
        Return the record in a dictionary

        :return: the current record
        :rtype: dict
        """
        return asdict(self)
