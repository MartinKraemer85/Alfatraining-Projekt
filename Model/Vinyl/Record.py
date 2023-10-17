from Model.ModelBase import *
from .Track import Track


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
            if key != "tracks":
                setattr(self, key, value)
                continue
            # also append the tracklist
            for track in value:
                self.tracks.append(self.generate_classinstance("Track", track))

    def generate_classinstance(self, name: str, properties: dict) -> any:
        """
        Generates a class instance via name and dictionary for the values.

        :param name: Class name
        :param properties: Properties
        :return:
        """
        print(properties)
        reference = globals()[name]
        instance = reference()
        instance.set_properties(properties)
        return instance

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
