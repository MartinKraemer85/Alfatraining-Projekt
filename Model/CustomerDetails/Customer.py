from Model.ModelBase import *


class Customer(ModelBase, Base):
    """
    A class that holds the Article properties

    """
    __tablename__ = 'customer'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(100))
    pwd: Mapped[str] = mapped_column(String(100))
