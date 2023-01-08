from datetime import date
from person.Person import Person
from common.base import sesion_factory


def create_people():
    sesion = sesion_factory()

    ali = Person("Ali", date(1993, 11, 20), 173, 84.5)
    sesion.add(ali)
    sesion.commit()
    sesion.close()


def get_people():
    sesion = sesion_factory()
    people_query = sesion.query(Person)
    sesion.close()
    return people_query.all()


if __name__ == '__main__':
    people = get_people()
    if len(people) == 0:
        create_people()

    people = get_people()

    for person in people:
        print(f"{person.name}, {person.date_of_birth}")
