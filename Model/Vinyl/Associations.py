from sqlalchemy import Float

from Model.ModelBase import *
from .Genre import Genre, SubGenre
from Model.SellerDetails.Seller import Seller


@dataclass()
class AscGenre(ModelBase, Base):
    __tablename__ = 'record_genre'
    __table_args__ = {'extend_existing': True}

    record_id: Mapped[int] = mapped_column(ForeignKey("record.id", ondelete="CASCADE"), primary_key=True)
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id", ondelete="CASCADE"), primary_key=True)
    genre: Mapped[Genre] = relationship(lazy="joined")


@dataclass()
class AscSubGenre(ModelBase, Base):
    __tablename__ = 'record_sub_genre'
    __table_args__ = {'extend_existing': True}

    record_id: Mapped[int] = mapped_column(ForeignKey("record.id", ondelete="CASCADE"), primary_key=True)
    sub_genre_id: Mapped[int] = mapped_column(ForeignKey("sub_genre.id", ondelete="CASCADE"), primary_key=True)
    sub_genre: Mapped[SubGenre] = relationship(lazy="joined")


@dataclass()
class AscSellerRecord(ModelBase, Base):
    __tablename__ = 'exemplar'
    __table_args__ = {'extend_existing': True}

    seller_id: Mapped[int] = mapped_column(ForeignKey("seller.id", ondelete="CASCADE"), primary_key=True)
    record_id: Mapped[int] = mapped_column(ForeignKey("record.id", ondelete="CASCADE"), primary_key=True)
    state: Mapped[int] = mapped_column(primary_key=True)
    price: Mapped[float] = mapped_column(Float(2))
    amount: Mapped[int] = mapped_column()
    dealer: Mapped[Seller] = relationship(lazy="joined")
