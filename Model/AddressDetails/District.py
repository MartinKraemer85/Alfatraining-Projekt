from ..ModelBase import *
from .City import City

@dataclass()
class District(ModelBase, Base):
    __tablename__ = 'district'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    zip_code: Mapped[str] = mapped_column(String(9))
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    addresses: Mapped[List["Address"]] = relationship(lazy="joined", cascade="all, delete")

    def set_properties(self, properties: dict) -> None:
        for key, value in properties.items():
            if key == "Model.AddressDetails.Address.Address":
                for address in value:
                    self.addresses.append(generate_classinstance(key, address))
                continue
            setattr(self, key, value)
