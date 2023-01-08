from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    text
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_connection_url = "postgresql://ojerfdbw:s2sK21OrGEeHBSEzJYp5F5qs4otnr_5D@hansken.db.elephantsql.com:5432/ojerfdbw"
base = declarative_base()
server = create_engine(db_connection_url, echo=True)


# CRUD => Create Read Update Delete
class Film(base):
    __tablename__ = "films"  # Tablo ismi
    id = Column(Integer, autoincrement=True, primary_key=True)
    title = Column(String)
    director = Column(String)
    year = Column(String)


session_instance = sessionmaker(server)
sesion = session_instance()
base.metadata.create_all(server)


def create_film():
    record = Film(
        title="Doctor Stranger",
        director="Scott Derrison",
        year="2016")
    sesion.add(record)
    sesion.commit()
    sesion.close()


# create_film()


def find_all_films():
    films = sesion.query(Film)  # select * from films
    for film in films:
        print(film.id, film.title, film.director, film.year)

    sesion.close()


# find_all_films()

def find_film_by_id(id: int):
    film = sesion.query(Film).filter(text("id = :id")).params(id=id).one()
    print(film.id, film.title, film.director, film.year)
    sesion.close()


# find_film_by_id(1)

def update_film_by_id(id: int):
    global record
    record = sesion.query(Film).filter(text("id = :id")).params(id=id).one()
    record.year = "2023"
    sesion.commit()
    sesion.close()


# update_film_by_id(1)
def delete_film_by_id(id: int):
    global record
    record = sesion.query(Film).filter(text("id = :id")).params(id=id).one()
    sesion.delete(record)
    sesion.commit()
    sesion.close()


delete_film_by_id(1)
