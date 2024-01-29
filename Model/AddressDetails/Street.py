from Model.ModelBase import *


@dataclass()
class Street(ModelBase, Base):
    __tablename__ = 'street'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column(String(10))
    name: Mapped[str] = mapped_column(String(70))
    district_id: Mapped[int] = mapped_column(ForeignKey("district.id"))
