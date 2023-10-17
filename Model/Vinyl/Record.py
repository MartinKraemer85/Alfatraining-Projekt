from .Track import Track
from ..ModelBase import *


@dataclass()
class Record(ModelBase):
    """
    A class that holds the Article properties

    """
    # title of the vinyl record
    title: str = None
    # the artist of the vinyl record
    artist: str = None
    # all record tracks
    tracks: list[Track] = field(default_factory=list)

    def set_properties(self, properties: dict) -> None:
        for key, value in properties.get("object").items():
            if key != "Model.Vinyl.Track.Track":
                setattr(self, key, value)
                continue
            # also append the tracklist
            for track in value:
                self.tracks.append(generate_classinstance("Model.Vinyl.Track.Track", track))

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
        :return: None
        """
        self.tracks.append(track)
