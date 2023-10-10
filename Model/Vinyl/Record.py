from dataclasses import dataclass, asdict, field
from .Track import *


@dataclass()
class Record:
    """
    A class that holds the Article properties

    """
    # title of the vinyl record
    title: str = None
    # the artist of the vinyl record
    artist: str = None
    # all record tracks
    tracks: list[Track] = field(default_factory=list)

    def dict(self) -> dict:
        """
        Return the record in a dictionary

        :return: the current record
        :rtype: dict
        """
        return asdict(self)

    def add_track(self, track: Track):
        """
        Add a new track to the list

        :param track: [Track]
        """
        self.tracks.append(track)

