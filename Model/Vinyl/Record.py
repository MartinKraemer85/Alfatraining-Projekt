from sqlalchemy import Integer, String

from .Track import Track
from ..ModelBase import *


@dataclass()
class Record(Base):
    """
    A class that holds the Article properties

    """

    __tablename__ = 'Record'
    id = Column(Integer, primary_key=True)
    # title of the vinyl record
    title = Column('title', String(100))
    # the artist of the vinyl record
    artist = Column('artist', String(100))
    # a list of all tracks
    # tracks: list[Track] = field(default_factory=list)
    # tracks: int = Column('artist', Integer())
    tracks = relationship("Track")

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
