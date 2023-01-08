from sqlalchemy import (
    Column,
    Integer,
    String,
    Date
)
from common.base import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    publish_date = Column(Date)

    def __init__(self, title, publish_date):
        self.title = title
        self.publish_date = publish_date
