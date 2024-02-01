from ..ModelBase import *
from .State import State

@dataclass()
class City(ModelBase, Base):
    __tablename__ = 'city'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    state_id: Mapped[int] = mapped_column(ForeignKey("state.id"))
    districts: Mapped[List["District"]] = relationship(lazy="joined", cascade="all, delete")

    def set_properties(self, properties: dict) -> None:
        for key, value in properties.items():
            if key == "Model.AddressDetails.District.District":
                for district in value:
                    self.districts.append(generate_classinstance(key, district))
                continue
            setattr(self, key, value)
