from common.base import sesion_factory
from User import User
from Mobile import Mobile


def populate_database():
    session = sesion_factory()

    ali = User("Ali")
    veli = User("Veli")

    ali_telefon = Mobile("poco xf3", "99999", ali)
    veli_telefon = Mobile("iphone 14 pro max", "5545", veli)

    session.add(ali_telefon)
    session.add(veli_telefon)

    session.commit()
    session.close()


def query_users():
    session = sesion_factory()

    users_query = session.query(User)
    session.close()
    return users_query.all()

def query_mobiles():
    sesion = sesion_factory()
    mobile_query = sesion.query(Mobile)
    sesion.close()
    return  mobile_query.all()



if __name__ == '__main__':

    users =  query_users()

    if len(users) == 0:
        populate_database()

    users =  query_users()

    for user in users:
        print(f"{user.name} , mobile model {user.mobile.model} number {user.mobile.number}")
