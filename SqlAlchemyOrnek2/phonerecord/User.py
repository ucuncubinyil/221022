from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.orm import relationship

from common.base import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    mobile = relationship("Mobile", uselist=False, backref="owner")

    def __init__(self, name):
        self.name = name
