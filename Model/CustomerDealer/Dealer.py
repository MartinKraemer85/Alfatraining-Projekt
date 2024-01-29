from Model.ModelBase import *


@dataclass()
class Dealer(ModelBase, Base):
    __tablename__ = 'dealer'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100))
    pwd: Mapped[str] = mapped_column(String(100))
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    mail: Mapped[str] = mapped_column(String(100))
    address_id: Mapped[int] = mapped_column(ForeignKey("address.id"))

