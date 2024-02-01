from ..ModelBase import *
from .Country import Country

@dataclass()
class State(ModelBase, Base):
    __tablename__ = 'state'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    state_name: Mapped[str] = mapped_column(String(30))
    state_initials: Mapped[str] = mapped_column(String(3))
    country_id: Mapped[int] = mapped_column(ForeignKey("country.id"))
    cities: Mapped[List["City"]] = relationship(lazy="joined", cascade="all, delete")

    def set_properties(self, properties: dict) -> None:
        for key, value in properties.items():
            if key == "Model.AddressDetails.City.City":
                for city in value:
                    self.cities.append(generate_classinstance(key, city))
                continue
            setattr(self, key, value)
