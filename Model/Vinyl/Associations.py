from sqlalchemy import Float

from Model.ModelBase import *
from .Genre import Genre, SubGenre
from Model.CustomerDealer.Dealer import Dealer


@dataclass()
class AscGenre(ModelBase, Base):
    __tablename__ = 'record_genre'
    __table_args__ = {'extend_existing': True}

    record_id: Mapped[int] = mapped_column(ForeignKey("record.id"), primary_key=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"), primary_key=True)
    genre: Mapped[Genre] = relationship(lazy="joined")


@dataclass()
class AscSubGenre(ModelBase, Base):
    __tablename__ = 'record_sub_genre'
    __table_args__ = {'extend_existing': True}

    record_id: Mapped[int] = mapped_column(ForeignKey("record.id"), primary_key=True)
    sub_genre_id: Mapped[int] = mapped_column(ForeignKey("sub_genre.id"), primary_key=True)
    sub_genre: Mapped[SubGenre] = relationship(lazy="joined")


@dataclass()
class AscDealerRecord(ModelBase, Base):
    __tablename__ = 'record_dealer'
    __table_args__ = {'extend_existing': True}

    dealer_id: Mapped[int] = mapped_column(ForeignKey("dealer.id"), primary_key=True)
    record_id: Mapped[int] = mapped_column(ForeignKey("record.id"), primary_key=True)
    state: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column(Float(2))
    amount: Mapped[int] = mapped_column()
    dealer: Mapped[Dealer] = relationship(lazy="joined")
