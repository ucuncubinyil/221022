### ABSTRACTION ###

"""
Abstract class (Soyut Sınıf):


"""

"""
from Bird import Bird

kus = Bird()
kus.walk()
kus.drink("Kaplan")
kus.sleep()

"""

"""
Bir E-Ticaret sitesinin Alt yapısını oluşturun
Product => id, name, price, stock, add , update, delete
Category => id, name, description, add, update,  delete
User => id,  name, lastname, password, email, gsm, add, update, delete => Member, Admin
Brad => id, name, description, add, update, delete

"""

from Product import Product

computer = Product()
computer.id = "1"
computer.name = "Levono"
computer.price = "5000$"
computer.stock = "50"
