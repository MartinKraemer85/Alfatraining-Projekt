from Model.ModelBase import *
from Model.AddressDetails import City, Country, District,State, Street


@dataclass()
class Address(ModelBase, Base):
    __tablename__ = 'address'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    # tracks: Mapped[List[City]] = relationship(lazy="immediate")
    # genres: Mapped[List[Country]] = relationship(lazy="immediate")
    # sub_genres: Mapped[List[District]] = relationship(lazy="immediate")
    # customer: Mapped[List[State]] = relationship(lazy="immediate")
    # customer: Mapped[List[Street]] = relationship(lazy="immediate")
