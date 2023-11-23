from sqlalchemy import Float
from .Track import Track
from ..ModelBase import *
from .Associations import AscSubGenre, AscGenre


# from .Genre import Genre, SubGenre


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
    type: Mapped[str] = mapped_column(String(100))
    year: Mapped[int] = mapped_column()
    state: Mapped[int] = mapped_column()
    price: Mapped[float] = mapped_column(Float(2))
    # todo: reviews?
    # lazy = "joined" : each Parent will also have its children collection populated
    tracks: Mapped[List[Track]] = relationship("Track", cascade="all, "
                                                                "delete-orphan",
                                               lazy="joined")
    genres: Mapped[List[AscGenre]] = relationship(lazy="joined")
    sub_genres: Mapped[List[AscSubGenre]] = relationship(lazy="joined")

    # reviews: Mapped[List['Review']] = relationship("Review", cascade="all, delete-orphan")

    def set_properties(self, properties: dict) -> None:
        for key, value in properties.get("attributes").items():
            if key != "Model.Vinyl.Track.Track":
                setattr(self, key, value)
                continue
            if key == "Model.Vinyl.Track.Track":
                # also append the tracklist if exists
                for track in value:
                    self.tracks.append(generate_classinstance("Model.Vinyl.Track.Track", track))

    def add_track(self, track: Track) -> None:
        """
        Add a new track to the list

        :param track: [Track]
        :return: None
        """
        self.tracks.append(track)

    def to_dict(self) -> dict:
        """
        Create a dictionary out of an object instance

        :return: object dict
        """
        # Since we want the relationships converted to a dict too, ignore them at first and add them separately
        # otherwise they would be added as Class object list
        ret = dict((f.name, getattr(self, f.name)) for f in fields(self) if f.name not in ['tracks', 'sub_genres', 'genres'])
        ret['tracks'] = [ track.to_dict() for track in self.tracks]
        ret['genres'] = [ track.to_dict() for track in self.genres]
        ret['sub_genres'] = [ track.to_dict() for track in self.sub_genres]
        return ret
