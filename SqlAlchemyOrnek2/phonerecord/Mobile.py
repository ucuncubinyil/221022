from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)

from common.base import Base


class Mobile(Base):
    __tablename__ = "mobile"

    id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(String)
    number = Column(String)
    owner_id = Column(Integer, ForeignKey("user.id"))

    def __init__(self, model, number, owner):
        self.model = model
        self.number = number
        self.owner = owner


