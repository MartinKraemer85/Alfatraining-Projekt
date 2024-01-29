from Model.ModelBase import *
from Model.AddressDetails.State import State

@dataclass()
class Country(ModelBase, Base):
    __tablename__ = 'country'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    country_name: Mapped[str] = mapped_column(String(30))
    country_initials: Mapped[str] = mapped_column(String(3))
    states: Mapped[List[State]] = relationship("State", lazy="joined")

    def set_properties(self, properties: dict) -> None:
        for key, value in properties.get("attributes").items():
            if key == "Model.AddressDetails.State.State":
                for state in value:
                    self.states.append(generate_classinstance(key, state))
                continue
            setattr(self, key, value)
