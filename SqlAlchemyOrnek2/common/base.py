from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_connection_url = "postgresql://ojerfdbw:s2sK21OrGEeHBSEzJYp5F5qs4otnr_5D@hansken.db.elephantsql.com:5432/ojerfdbw"
server = create_engine(db_connection_url, echo=True)


session_instance = sessionmaker(server)
sesion = session_instance()

Base = declarative_base()


def sesion_factory():
    Base.metadata.create_all(server)
    return sesion
