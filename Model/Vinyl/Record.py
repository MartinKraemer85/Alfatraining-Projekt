from .Track import Track
from ..ModelBase import *


@dataclass()
class Record(ModelBase, Base):
    """
    A class that holds the Article properties

    """
    __tablename__ = 'record'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    artist: Mapped[str] = mapped_column(String(100))

    tracks: Mapped[List['Track']] = relationship("Track", cascade="all, delete-orphan")

    def set_properties(self, properties: dict) -> None:
        for key, value in properties.get("attributes").items():
            if key != "Model.Vinyl.Track.Track":
                setattr(self, key, value)
                continue
            if key == "Model.Vinyl.Track.Track":
                # also append the tracklist if exists
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
