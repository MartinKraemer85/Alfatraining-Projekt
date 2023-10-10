from dataclasses import dataclass, asdict
from datetime import time


@dataclass()
class Track:
    """
    A class that holds the Article properties

    """
    # title of the vinyl record
    title: str = None
    # the artist of the vinyl record
    length: time = None

    def dict(self) -> dict:
        """
        Return the record in a dictionary

        :return: the current record
        :rtype: dict
        """
        return asdict(self)
