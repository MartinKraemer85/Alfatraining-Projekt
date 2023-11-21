from Model.ModelBase import *
from .Genre import Genre


@dataclass()
class AscGenre(ModelBase, Base):
    __tablename__ = 'record_genre'
    __table_args__ = {'extend_existing': True}

    record_id: Mapped[int] = mapped_column(ForeignKey("record.id"), primary_key=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"), primary_key=True)
    genre: Mapped[Genre] = relationship()


@dataclass()
class AscSubGenre(ModelBase, Base):
    __tablename__ = 'record_sub_genre'
    __table_args__ = {'extend_existing': True}

    record_id: Mapped[int] = mapped_column(ForeignKey("record.id"), primary_key=True)
    sub_genre_id: Mapped[int] = mapped_column(ForeignKey("sub_genre.id"), primary_key=True)
    sub_genre: Mapped['SubGenre'] = relationship()
