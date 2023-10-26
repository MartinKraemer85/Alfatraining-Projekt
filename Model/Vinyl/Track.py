from Model.ModelBase import *


@dataclass()
class Track(ModelBase, Base):
    """
    A class that holds the Article properties

    """
    __tablename__ = 'track'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    record_id: Mapped[int] = mapped_column(ForeignKey("record.id"))
    # title of the vinyl record
    name: Mapped[str] = mapped_column(String(100))
    # the artist of the vinyl record
    length: Mapped[str] = mapped_column(String(50))

    def set_properties(self, properties: dict) -> None:
        for key, value in properties.items():
            setattr(self, key, value)

    def dict(self) -> dict:
        """
        Return the record in a dictionary

        :return: the current record
        :rtype: dict
        """
        return asdict(self)
