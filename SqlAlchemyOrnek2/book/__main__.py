from datetime import date
from book.Book import Book
from common.base import sesion_factory


def create_book():
    session = sesion_factory()
    java18 = Book("Java 18", date(2023, 1, 1))
    session.add(java18)
    session.commit()
    session.close()


def get_books():
    session = sesion_factory()
    books = session.query(Book)
    session.close()
    return books.all()


if __name__ == '__main__':

    books = get_books()

    if len(books) == 0:
        create_book()

    books = get_books()

    for book in books:
        print(f"Book name: {book.title}, publish date {book.publish_date}")
