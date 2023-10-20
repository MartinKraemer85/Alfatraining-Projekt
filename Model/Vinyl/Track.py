from datetime import time

from Model.ModelBase import *


@dataclass()
class Track(Base):
    """
    A class that holds the Article properties

    """
    __tablename__ = 'Track'
    id = Column(Integer, primary_key=True)
    record_id = Column(Integer, ForeignKey("Record.id"), nullable=False)
    # title of the vinyl record
    title = Column('title', String(100))
    # the artist of the vinyl record
    length = Column('length', Time())

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
