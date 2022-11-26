from datetime import date


def age(birth_date: date):
    today = date.today()
    one_or_zero = ((today.month, today.day) < (birth_date.month, birth_date.day))
    year_differance = today.year - birth_date.year
    age = year_differance - one_or_zero
    return age
