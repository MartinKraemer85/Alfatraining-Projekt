from Model.AddressDetails.Street import Street
from Model.ModelBase import *


@dataclass()
class District(ModelBase, Base):
    __tablename__ = 'district'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    zip_code: Mapped[str] = mapped_column(String(9))
    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    streets: Mapped[List[Street]] = relationship("Street", lazy="joined")

    def set_properties(self, properties: dict) -> None:
        for key, value in properties.items():
            if key == "Model.AddressDetails.Street.Street":
                for street in value:
                    self.streets.append(generate_classinstance(key, street))
                continue
            setattr(self, key, value)
