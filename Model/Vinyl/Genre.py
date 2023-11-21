from Model.ModelBase import *


@dataclass()
class Genre(ModelBase, Base):
    __tablename__ = 'genre'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))


@dataclass()
class SubGenre(ModelBase, Base):
    __tablename__ = "sub_genre"
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
